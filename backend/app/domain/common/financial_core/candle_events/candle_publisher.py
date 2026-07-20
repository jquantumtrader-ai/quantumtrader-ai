from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable

from ..candles import Candle


class CandlePublisher(ABC):
    """
    Contrato para publicação de candles.
    """

    @abstractmethod
    def publish(self, candle: Candle) -> None:
        ...

    @abstractmethod
    def subscribe(
        self,
        callback: Callable[[Candle], None],
    ) -> None:
        ...
