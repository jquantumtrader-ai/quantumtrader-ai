from dataclasses import dataclass
from abc import ABC


@dataclass(
    frozen=True,
    slots=True
)
class ValueObject(ABC):
    """
    Classe base dos Value Objects.

    Características:

    - Imutável
    - Hashável
    - Comparável
    """

    def to_dict(self):

        return {
            key: value
            for key, value
            in self.__dict__.items()
        }
