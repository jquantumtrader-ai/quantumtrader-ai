from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4


@dataclass(frozen=True)
class OrderId:
    """
    Identificador único de uma ordem.

    Utiliza UUID v4 para garantir unicidade.
    """

    value: UUID

    @classmethod
    def new(
        cls,
    ) -> "OrderId":
        """
        Cria um novo identificador.
        """

        return cls(
            uuid4(),
        )

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> "OrderId":
        """
        Reconstrói um OrderId a partir de uma string.
        """

        return cls(
            UUID(value),
        )

    def __str__(
        self,
    ) -> str:

        return str(
            self.value,
        )
