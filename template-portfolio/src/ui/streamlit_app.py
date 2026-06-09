"""Google Python Code Reviewer - Streamlit UI."""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

# Adiciona o root do projeto no path para imports
_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT))

load_dotenv()

import streamlit as st

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Google Python Reviewer",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

from src.pipeline.rag import build_rag_pipeline
from src.pipeline.cache import ExactCache, SemanticCache
from src.observability.trace import trace, log_event
from src.pipeline.routing import classify_complexity

# ==========================================
# CACHE E INICIALIZAÇÃO
# ==========================================
@st.cache_resource
def get_pipeline():
    # Inicializa o pipeline silenciosamente e usa cache
    return build_rag_pipeline(corpus_dir=str(_ROOT / "data" / "corpus"))

@st.cache_resource
def init_caches():
    return ExactCache(), SemanticCache()

# ==========================================
# INTERFACE PRINCIPAL
# ==========================================
def main():
    # Carrega backend
    with st.spinner("Inicializando o motor de inteligência..."):
        pipeline = get_pipeline()
        exact_cache, semantic_cache = init_caches()

    # SIDEBAR: Configurações e Status
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=60)
        st.title("Configurações")
        st.markdown("Bem-vindo ao **Google Python Code Reviewer**.")
        st.divider()
        
        st.subheader("📊 Status do Sistema")
        st.metric("Documentos no Banco", pipeline.collection.count())
        st.metric("Cache Exato (Itens)", exact_cache.stats()["size"])
        st.metric("Cache Semântico (Itens)", semantic_cache.stats()["size"])
        
        st.divider()
        if st.button("🗑️ Limpar Histórico e Caches", use_container_width=True):
            init_caches.clear()
            st.session_state.messages = []
            st.success("Tudo limpo!")

    # ÁREA PRINCIPAL
    st.title("🐍 Google Python Code Reviewer")
    st.markdown(
        "Este assistente utiliza **RAG (Retrieval-Augmented Generation)** com modelos de ponta para validar seu código "
        "ou tirar dúvidas usando o [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) como fonte da verdade."
    )
    st.divider()

    # Inicializa estado do chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe histórico do chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander("📚 Fontes Citadas (Google Style Guide)"):
                    for source, page in msg["sources"]:
                        st.write(f"- `{source}`")

    # Layout para Atalhos/Ações Rápidas (só mostra se o chat estiver vazio)
    query_suggestion = None
    if not st.session_state.messages:
        st.markdown("### Ações Rápidas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("**Dúvidas de Estilo**")
            if st.button("Como usar decorators?"):
                query_suggestion = "Explique detalhadamente como usar decorators segundo o guia de estilo."
        with col2:
            st.warning("**Arquitetura**")
            if st.button("Regras de Importação?"):
                query_suggestion = "Quais são as regras estritas para importações no início dos arquivos?"
        with col3:
            st.success("**Revisão de Código**")
            if st.button("Revisar Código de Exemplo"):
                query_suggestion = "Analise este código e aponte os erros de estilo:\n\n```python\nimport sys, os\ndef Teste():\n  pass\n```"

    # Captura a entrada do usuário
    query = st.chat_input("Digite sua dúvida ou cole seu código Python aqui...")
    if query_suggestion:
        query = query_suggestion

    if query:
        # Exibe mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Processa a resposta
        with st.chat_message("assistant"):
            with trace("query_handle", query=query) as ctx:
                trace_id = ctx["trace_id"]
                result = None
                
                # 1. Verifica Cache Exato
                cached = exact_cache.get(query)
                if cached:
                    log_event("cache_hit", trace_id=trace_id, layer="exact")
                    result = {"answer": cached, "sources": []}
                    st.caption("⚡ Respondido instantaneamente pelo Cache Exato!")

                # 2. Verifica Cache Semântico
                if not result:
                    try:
                        cached = semantic_cache.get(query)
                        if cached:
                            log_event("cache_hit", trace_id=trace_id, layer="semantic")
                            result = {"answer": cached, "sources": []}
                            st.caption("🧠 Respondido rapidamente pelo Cache Semântico!")
                    except NotImplementedError:
                        pass
                
                # 3. Processamento RAG Completo
                if not result:
                    with st.spinner("Analisando o Guia de Estilo do Google..."):
                        try:
                            decision = classify_complexity(query)
                            log_event("route_decision", trace_id=trace_id, **decision.__dict__)
                            pipeline.llm_model = decision.model
                            
                            if "70b" in decision.model:
                                st.caption(f"🤖 Usando inteligência avançada: `{decision.model}`")
                        except NotImplementedError:
                            pass
                        
                        try:
                            result = pipeline.answer(query)
                        except Exception as e:
                            st.error(f"Ocorreu um erro no pipeline RAG: {e}")
                            st.stop()

                        # Salva nos caches
                        exact_cache.put(query, result["answer"])
                        semantic_cache.put(query, result["answer"])
                        log_event("answer_generated", trace_id=trace_id, sources=len(result.get("sources", [])))

                # Exibe a resposta final
                st.markdown(result["answer"])
                
                # Exibe as fontes se existirem
                if result.get("sources"):
                    with st.expander("📚 Fontes Citadas (Google Style Guide)"):
                        for source, page in set(result["sources"]):  # Usa set() para evitar duplicados
                            st.write(f"- `{source}`")
                
                # Salva o assistant no histórico
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result.get("sources", [])
                })

if __name__ == "__main__":
    main()
