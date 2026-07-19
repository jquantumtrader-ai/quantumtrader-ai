from __future__ import annotations

from uuid import UUID

from ..aggregates import ExecutionAggregate


class InMemoryExecutionRepository:
    """
    Adapter em memória para armazenamento
    de Execution Aggregate.

    Implementa o contrato ExecutionRepository.
    """

    def __init__(self) -> None:

        self._storage: dict[
            UUID,
            ExecutionAggregate,
        ] = {}


    def save(
        self,
        execution: ExecutionAggregate,
    ) -> None:
        """
        Salva ou atualiza uma execução.
        """

        self._storage[
            execution.execution_id
        ] = execution



    def get(
        self,
        execution_id: UUID,
    ) -> ExecutionAggregate:
        """
        Recupera uma execução.
        """

        try:

            return self._storage[
                execution_id
            ]

        except KeyError as exc:

            raise ValueError(
                "Execution not found"
            ) from exc



    def exists(
        self,
        execution_id: UUID,
    ) -> bool:
        """
        Verifica se existe.
        """

        return (
            execution_id
            in
            self._storage
        )



    def remove(
        self,
        execution_id: UUID,
    ) -> None:
        """
        Remove uma execução.
        """

        try:

            del self._storage[
                execution_id
            ]

        except KeyError as exc:

            raise ValueError(
                "Execution not found"
            ) from exc



    def clear(self) -> None:
        """
        Limpa armazenamento.
        """

        self._storage.clear()
