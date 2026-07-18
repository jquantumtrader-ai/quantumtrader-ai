from __future__ import annotations

from .simulation_result import SimulationResult
from ..rebalance_plan import RebalancePlan


class PortfolioSimulation:
    """
    Placeholder para o simulador de rebalanceamento.

    A implementação será concluída quando o
    Order Engine estiver disponível.
    """

    def simulate(
        self,
        plan: RebalancePlan,
    ) -> SimulationResult:
        raise NotImplementedError(
            "PortfolioSimulation será implementado após o Order Engine."
        )
