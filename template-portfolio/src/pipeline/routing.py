"""Model routing cheap-first com fallback."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class RouteDecision:
    model: str
    complexity: str  # "simple" | "complex"
    reason: str


# ------------------------------------------------------------------ TODO 6
def classify_complexity(query: str) -> RouteDecision:
    """Classifica complexidade da query para escolher modelo (cheap vs premium)."""
    cheap_model = os.environ.get("CHEAP_MODEL", "llama-3.1-8b-instant")
    premium_model = os.environ.get("PREMIUM_MODEL", "llama-3.3-70b-versatile")

    q_lower = query.lower()
    complex_keywords = ["analise", "revise", "verifique", "avalie", "código", "codigo", "def ", "class "]

    is_complex = False
    if len(query) > 150:
        is_complex = True
        reason = "A query é longa (mais de 150 caracteres)"
    elif any(kw in q_lower for kw in complex_keywords):
        is_complex = True
        reason = "A query requer análise avançada ou inspeção de código"
    else:
        reason = "A query é direta e curta"

    if is_complex:
        return RouteDecision(model=premium_model, complexity="complex", reason=reason)
    else:
        return RouteDecision(model=cheap_model, complexity="simple", reason=reason)
