from __future__ import annotations

from abc import ABC, abstractmethod

from ..models.allocation_request import (
    AllocationRequest,
)

from ..models.allocation_result import (
    AllocationResult,
)


class AllocationPolicy(ABC):
    """
    Contrato base para políticas de alocação financeira.

    Uma Policy define a regra de distribuição.
    A execução matemática fica nos Allocators.
    """


    @abstractmethod
    def allocate(
        self,
        request: AllocationRequest,
    ) -> list[AllocationResult]:
        """
        Executa uma política de alocação.

        Parameters
        ----------
        request:
            Dados completos da alocação.

        Returns
        -------
        list[AllocationResult]
            Resultado detalhado da distribuição.
        """

        raise NotImplementedError
