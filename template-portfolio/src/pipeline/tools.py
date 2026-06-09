"""Function-calling / tool-use — registro de tools usadas pelo agente."""

from __future__ import annotations

import json
import subprocess
from typing import Any, Callable


# ============================================================================
# TODO 4 — Sua tool especifica do dominio
# ============================================================================

def run_linter(code: str) -> str:
    """Roda `ruff check` no snippet e retorna lista de erros."""
    try:
        # Pass the code through stdin and read stdout/stderr.
        result = subprocess.run(
            ["ruff", "check", "--stdin-filename=tmp.py", "-"],
            input=code,
            text=True,
            capture_output=True,
            check=False
        )
        if result.stdout:
            return result.stdout
        elif result.stderr:
            return result.stderr
        else:
            return "Nenhum erro encontrado pelo Ruff. O código está seguindo as regras de lint do Ruff perfeitamente."
    except Exception as e:
        return f"Erro executando o linter. Verifique se o 'ruff' está instalado. Erro: {e}"


TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "run_linter",
            "description": "Roda a ferramenta determinística de linting (Ruff) em um snippet de código Python para procurar por erros de sintaxe ou de estilo. Retorna a saída do Ruff (erros e warnings detectados).",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "O snippet de código Python que deve ser analisado pelo linter."},
                },
                "required": ["code"],
            },
        },
    },
]


TOOL_REGISTRY: dict[str, Callable[..., str]] = {
    "run_linter": run_linter,
}


def run_tool_call(name: str, arguments_json: str) -> str:
    """Executa uma tool call e retorna o resultado como string."""
    if name not in TOOL_REGISTRY:
        return f"ERROR: tool '{name}' nao registrada"
    try:
        kwargs = json.loads(arguments_json)
        return TOOL_REGISTRY[name](**kwargs)
    except Exception as e:
        return f"ERROR ao executar {name}: {e}"
