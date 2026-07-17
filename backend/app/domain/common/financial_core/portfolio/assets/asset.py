from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Asset:
    """
    Representa a identidade de um ativo financeiro.

    Exemplos:

    PETR4
    VALE3
    BTCUSDT
    WINQ26
    """

    symbol: str


    def __post_init__(self) -> None:
        """
        Normaliza e valida o símbolo.
        """

        normalized = self.symbol.strip().upper()


        if not normalized:
            raise ValueError(
                "Símbolo do ativo não pode ser vazio."
            )


        object.__setattr__(
            self,
            "symbol",
            normalized,
        )


    def __str__(self) -> str:
        return self.symbol
