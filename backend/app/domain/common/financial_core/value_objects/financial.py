from __future__ import annotations

from decimal import Decimal

from .numeric import NumericValue


class FinancialValue(NumericValue):
    """
    Classe base para todos os valores financeiros.

    Responsabilidades:
    - Define precisão financeira
    - Possui utilidades de arredondamento
    - Padroniza serialização
    """

    SCALE = Decimal("0.00000001")

    def quantize(self) -> FinancialValue:
        """
        Retorna um novo valor arredondado para a
        precisão financeira padrão.
        """
        return FinancialValue(
            self.value.quantize(self.SCALE)
        )

    def as_decimal(self) -> Decimal:
        """
        Retorna o Decimal interno.
        """
        return self.value

    def as_float(self) -> float:
        """
        Conversão para float apenas quando necessário.
        """
        return float(self.value)

    def as_string(self) -> str:
        """
        Representação textual do valor.
        """
        return str(self.value)
