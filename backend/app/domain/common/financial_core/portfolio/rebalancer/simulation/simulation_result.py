from __future__ import annotations

from dataclasses import dataclass

from ....portfolio.portfolio import Portfolio


@dataclass(frozen=True)
class SimulationResult:
    """
    Resultado da simulação do rebalanceamento.
    """

    portfolio: Portfolio
