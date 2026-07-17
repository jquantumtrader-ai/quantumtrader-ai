from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from ..value_objects.money import Money


class MoneyAllocator(ABC):
    """
    Contrato para algoritmos de alocação monetária.

    Implementações concretas deverão dividir um
    valor monetário em múltiplas parcelas.
    """

    @abstractmethod
    def allocate(
        self,
        money: Money,
        ratios: list[int],
    ) -> list[Money]:
        """
        Divide um valor monetário conforme
        os pesos informados.
        """
        raise NotImplementedError
