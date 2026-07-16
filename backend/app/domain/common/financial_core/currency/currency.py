from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Currency:
    """
    Representa uma moeda negociável.
    """

    code: str
    symbol: str
    name: str

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return f"Currency(code='{self.code}')"
