from __future__ import annotations

from dataclasses import dataclass, field

from ..queries import OrderQueryModel


@dataclass(slots=True)
class OrderReadStore:
    """
    Armazenamento de leitura
    para Query Models de Ordens.

    Primeira implementação:
    armazenamento em memória.
    """

    _storage: dict[
        str,
        OrderQueryModel,
    ] = field(
        default_factory=dict,
    )

    def write(
        self,
        query: OrderQueryModel,
    ) -> None:
        """
        Persiste um Query Model.
        """

        self._storage[
            query.order_id
        ] = query

    def read(
        self,
        order_id: str,
    ) -> OrderQueryModel | None:
        """
        Recupera um Query Model.
        """

        return self._storage.get(
            order_id,
        )

    def read_all(
        self,
    ) -> list[OrderQueryModel]:
        """
        Recupera todos os Query Models.
        """

        return list(
            self._storage.values(),
        )

    def delete(
        self,
        order_id: str,
    ) -> None:
        """
        Remove um Query Model.
        """

        self._storage.pop(
            order_id,
            None,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove todos os registros.
        """

        self._storage.clear()

    def count(
        self,
    ) -> int:
        """
        Retorna quantidade
        de registros.
        """

        return len(
            self._storage,
        )
