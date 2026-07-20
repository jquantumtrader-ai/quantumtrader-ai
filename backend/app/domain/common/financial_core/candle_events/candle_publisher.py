from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable

from ..candles import Candle


class CandlePublisher(ABC):
    @abstractmethod
    def publish(self, candle: Candle) -> None:
        raise NotImplementedError

    @abstractmethod
    def subscribe(
        self,
        subscriber: Callable[[Candle], None],
    ) -> None:
        raise NotImplementedError
