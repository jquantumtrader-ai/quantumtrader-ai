from .currency import Currency
from .predefined import BRL, USD, EUR, BTC, ETH


class CurrencyRegistry:
    """
    Registro central de moedas suportadas.
    """

    _currencies: dict[str, Currency] = {
        BRL.code: BRL,
        USD.code: USD,
        EUR.code: EUR,
        BTC.code: BTC,
        ETH.code: ETH,
    }

    @classmethod
    def get(cls, code: str) -> Currency:
        return cls._currencies[code]

    @classmethod
    def exists(cls, code: str) -> bool:
        return code in cls._currencies

    @classmethod
    def all(cls) -> tuple[Currency, ...]:
        return tuple(cls._currencies.values())
