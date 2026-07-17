from __future__ import annotations

from abc import ABC
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(
    frozen=True,
    slots=True,
)
class ValueObject(ABC):
    """
    Classe base para todos os Value Objects do domínio.

    Características:

    - Imutável
    - Hashável
    - Comparável
    - Serializável
    """

    def to_dict(self) -> dict[str, Any]:
        """
        Converte o Value Object em um dicionário.

        Utiliza a serialização oficial do dataclass,
        suportando objetos aninhados.
        """
        return asdict(self)
