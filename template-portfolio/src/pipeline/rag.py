"""RAG pipeline — chunk, embed, index, retrieve, generate.

Reaproveita as funcoes do notebook 02.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any
import json

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI

from src.pipeline.tools import TOOLS, run_tool_call


def _make_client() -> OpenAI:
    """Inicializa cliente OpenAI-compatible conforme provider escolhido no .env."""
    if "GROQ_API_KEY" in os.environ:
        return OpenAI(
            api_key=os.environ["GROQ_API_KEY"],
            base_url="https://api.groq.com/openai/v1",
        )
    elif "GEMINI_API_KEY" in os.environ:
        return OpenAI(
            api_key=os.environ["GEMINI_API_KEY"],
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
    elif "OPENAI_API_KEY" in os.environ:
        return OpenAI()
    else:
        raise RuntimeError("Configure GROQ_API_KEY ou OPENAI_API_KEY no .env")


class RAGPipeline:
    """Pipeline RAG end-to-end com Chroma local."""

    def __init__(
        self,
        corpus_dir: str = "data/corpus",
        persist_dir: str = "data/chroma",
        collection_name: str = "docs",
        llm_model: str | None = None,
    ) -> None:
        self.client = _make_client()
        self.llm_model = llm_model or os.environ.get("LLM_MODEL", "llama-3.1-8b-instant")

        # Usando modelo multilingual para suportar queries em PT-BR contra corpus em Inglês
        self.embed_fn = SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")

        self.corpus_dir = Path(corpus_dir)
        self.persist_dir = persist_dir
        self.collection_name = collection_name

        chroma = chromadb.PersistentClient(path=persist_dir)
        self.collection = chroma.get_or_create_collection(
            name=collection_name, embedding_function=self.embed_fn
        )

    # ------------------------------------------------------------------ TODO 1
    def ingest_and_index(self) -> int:
        """Le MD/PDFs de `corpus_dir`, faz chunking e indexa em Chroma."""
        docs: list[dict] = []
        for file_path in self.corpus_dir.glob("**/*.*"):
            if file_path.suffix == ".md" or file_path.suffix == ".txt":
                try:
                    text = file_path.read_text(encoding="utf-8")
                    docs.append({"text": text, "source": file_path.name, "page": 1})
                except Exception as e:
                    print(f"Erro lendo {file_path}: {e}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        chunks: list[dict] = []
        for doc in docs:
            splits = splitter.split_text(doc["text"])
            for i, chunk_text in enumerate(splits):
                chunks.append({
                    "id": f"{doc['source']}-{doc['page']}-{i}",
                    "text": chunk_text,
                    "source": doc["source"],
                    "page": doc["page"]
                })

        if not chunks:
            return 0

        # Adicionar chunks no Chroma via self.collection.add
        ids = [c["id"] for c in chunks]
        texts = [c["text"] for c in chunks]
        metadatas = [{"source": c["source"], "page": c["page"]} for c in chunks]

        # Batch add to avoid max limits
        batch_size = 5000
        for i in range(0, len(ids), batch_size):
            self.collection.add(
                ids=ids[i:i+batch_size],
                documents=texts[i:i+batch_size],
                metadatas=metadatas[i:i+batch_size]
            )

        return self.collection.count()

    # ------------------------------------------------------------------ TODO 2
    def retrieve(self, query: str, k: int = 5) -> list[dict]:
        """Busca top-k chunks similares a query."""
        results = self.collection.query(query_texts=[query], n_results=k)

        hits = []
        if results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                dist = results["distances"][0][i] if "distances" in results and results["distances"] else 0.0
                hits.append({
                    "text": results["documents"][0][i],
                    "source": results["metadatas"][0][i]["source"],
                    "page": results["metadatas"][0][i]["page"],
                    "distance": dist
                })
        return hits

    # ------------------------------------------------------------------ TODO 3
    def answer(self, question: str, k: int = 5) -> dict:
        """Pipeline completo: retrieve + augment + generate. Retorna {answer, sources}."""
        hits = self.retrieve(question, k=k)

        context_parts = []
        sources = []
        for h in hits:
            context_parts.append(f"[{h['source']}:{h['page']}]\n{h['text']}")
            sources.append((h['source'], h['page']))

        context = "\n\n".join(context_parts)

        prompt = PROMPT_TEMPLATE.format(context=context, question=question)

        messages = [
            {"role": "system", "content": "Você é um Code Reviewer Sênior em Python. Sua função principal é ajudar os usuários consultando os trechos de documentação que o sistema te envia. Ignore a presença de tags HTML (como <p>, <span>) no contexto e foque no texto útil para responder. Use a tool run_linter se o usuário fornecer um código para validação de estilo."},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.llm_model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.2,
            presence_penalty=0.5,
            frequency_penalty=0.5
        )

        message = response.choices[0].message

        if message.tool_calls:
            for tool_call in message.tool_calls:
                func_name = tool_call.function.name
                func_args = tool_call.function.arguments
                tool_result = run_tool_call(func_name, func_args)

                messages.append(message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": func_name,
                    "content": tool_result
                })

            response2 = self.client.chat.completions.create(
                model=self.llm_model,
                messages=messages,
                temperature=0.2,
                presence_penalty=0.5,
                frequency_penalty=0.5
            )
            answer = response2.choices[0].message.content
        else:
            answer = message.content

        return {"answer": answer, "sources": sources}


PROMPT_TEMPLATE = """Você é um assistente técnico especializado no Google Python Style Guide.
Abaixo você receberá trechos retirados diretamente do guia oficial. Alguns trechos podem conter formatação HTML/Markdown. Extraia a informação relevante e responda a pergunta do usuário de forma clara e profissional.

Se a informação não estiver no contexto de forma alguma, responda: "Não encontrado no corpus de estilo."

SEMPRE cite a regra no final da sua explicação, utilizando o formato: [nome_do_arquivo].

CONTEXTO DO STYLE GUIDE:
{context}

PERGUNTA: {question}

RESPOSTA CLARA E DETALHADA:"""


def build_rag_pipeline(corpus_dir: str = "data/corpus") -> RAGPipeline:
    """Factory: cria pipeline e indexa corpus se ainda nao indexado."""
    pipeline = RAGPipeline(corpus_dir=corpus_dir)
    if pipeline.collection.count() == 0:
        pipeline.ingest_and_index()
    return pipeline
