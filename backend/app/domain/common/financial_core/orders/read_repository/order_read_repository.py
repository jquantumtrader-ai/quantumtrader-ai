from __future__ import annotations

from dataclasses import dataclass, field

from ..queries import OrderQueryModel


@dataclass(slots=True)
class OrderReadRepository:
    """
    Repositório de leitura (CQRS Read Repository).

    Nesta primeira implementação o armazenamento
    é mantido em memória.
    """

    _orders: dict[str, OrderQueryModel] = field(
        default_factory=dict,
    )

    def save(
        self,
        order: OrderQueryModel,
    ) -> None:
        """
        Salva ou atualiza um Query Model.
        """

        self._orders[
            order.order_id
        ] = order

    def get(
        self,
        order_id: str,
    ) -> OrderQueryModel | None:
        """
        Recupera uma ordem pelo identificador.
        """

        return self._orders.get(
            order_id,
        )

    def list_all(
        self,
    ) -> list[OrderQueryModel]:
        """
        Retorna todas as ordens.
        """

        return list(
            self._orders.values(),
        )

    def exists(
        self,
        order_id: str,
    ) -> bool:
        """
        Verifica se a ordem existe.
        """

        return (
            order_id
            in self._orders
        )

    def count(
        self,
    ) -> int:
        """
        Retorna a quantidade de ordens.
        """

        return len(
            self._orders,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove todas as ordens.
        """

        self._orders.clear()
