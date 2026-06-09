"""Cache em 2 niveis: exact-match (SHA256) + semantic (cosine similarity)."""

from __future__ import annotations

import hashlib
from typing import Any

import numpy as np
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction


class ExactCache:
    """Cache por hash SHA256 da query. Captura replays exatos (~10-15% das queries)."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    @staticmethod
    def _key(query: str) -> str:
        return hashlib.sha256(query.encode()).hexdigest()

    def get(self, query: str) -> str | None:
        return self._store.get(self._key(query))

    def put(self, query: str, answer: str) -> None:
        self._store[self._key(query)] = answer

    def stats(self) -> dict[str, int]:
        return {"size": len(self._store)}


class SemanticCache:
    """Cache por similaridade de embedding. Captura parafrases (~20% adicional)."""

    def __init__(self, threshold: float = 0.93) -> None:
        self.threshold = threshold
        self._queries: list[str] = []
        self._embeddings: list[np.ndarray] = []
        self._answers: list[str] = []

        # Usando a mesma embedding function local (MiniLM) para não usar cota
        self._embed_fn = DefaultEmbeddingFunction()

    def _embed(self, text: str) -> np.ndarray:
        embedding = self._embed_fn([text])[0]
        return np.array(embedding)

    # ------------------------------------------------------------------ TODO 5
    def get(self, query: str) -> str | None:
        """Retorna resposta cacheada se similar a query alguma anterior, OU None."""
        if not self._queries:
            return None

        e = self._embed(query)
        best_sim = -1.0
        best_idx = -1

        for idx, em in enumerate(self._embeddings):
            norm_e = np.linalg.norm(e)
            norm_em = np.linalg.norm(em)
            if norm_e == 0 or norm_em == 0:
                continue
            cos_sim = np.dot(e, em) / (norm_e * norm_em)
            if cos_sim > best_sim:
                best_sim = cos_sim
                best_idx = idx

        if best_sim >= self.threshold:
            return self._answers[best_idx]

        return None

    def put(self, query: str, answer: str) -> None:
        self._queries.append(query)
        self._embeddings.append(self._embed(query))
        self._answers.append(answer)

    def stats(self) -> dict[str, Any]:
        return {"size": len(self._queries), "threshold": self.threshold}
