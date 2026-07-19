from __future__ import annotations

from ..ports import ExecutionRepository


class ExecutionUnitOfWork:
    """
    Unidade de trabalho responsável por controlar
    o ciclo transacional das operações de execução.
    """


    def __init__(
        self,
        repository: ExecutionRepository,
    ) -> None:

        self._repository = repository

        self._active = False

        self._committed = False

        self._rolled_back = False



    @property
    def repository(
        self,
    ) -> ExecutionRepository:
        """
        Retorna o repository da transação.
        """

        return self._repository



    def begin(
        self,
    ) -> None:
        """
        Inicia uma unidade de trabalho.
        """

        self._active = True

        self._committed = False

        self._rolled_back = False



    def commit(
        self,
    ) -> None:
        """
        Confirma a transação.
        """

        if not self._active:

            raise RuntimeError(
                "Unit of work is not active"
            )


        self._committed = True

        self._active = False



    def rollback(
        self,
    ) -> None:
        """
        Reverte a transação.
        """

        if not self._active:

            raise RuntimeError(
                "Unit of work is not active"
            )


        self._rolled_back = True

        self._active = False



    @property
    def is_active(
        self,
    ) -> bool:
        return self._active



    @property
    def is_committed(
        self,
    ) -> bool:
        return self._committed



    @property
    def is_rolled_back(
        self,
    ) -> bool:
        return self._rolled_back
