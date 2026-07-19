from __future__ import annotations

from decimal import Decimal
from typing import Protocol
from uuid import UUID

from ..aggregates import ExecutionAggregate


class ExecutionRepository(Protocol):
    """
    Contrato de persistência
    para Execution Aggregate.
    """


    def create(
        self,
        execution_id: UUID,
        quantity: Decimal,
    ) -> ExecutionAggregate:
        """
        Cria uma nova execução.
        """
        ...



    def save(
        self,
        execution: ExecutionAggregate,
    ) -> None:
        """
        Persiste uma execução.
        """
        ...



    def get(
        self,
        execution_id: UUID,
    ) -> ExecutionAggregate:
        """
        Recupera uma execução.
        """
        ...



    def exists(
        self,
        execution_id: UUID,
    ) -> bool:
        """
        Verifica existência.
        """
        ...



    def remove(
        self,
        execution_id: UUID,
    ) -> None:
        """
        Remove uma execução.
        """
        ...
