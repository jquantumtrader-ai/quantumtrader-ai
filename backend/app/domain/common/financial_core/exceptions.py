class FinancialCoreException(Exception):
    """
    Exceção base do Financial Core.
    """
    pass


class InvalidValueException(
    FinancialCoreException
):
    """
    Valor inválido para um objeto financeiro.
    """
    pass


class InvalidOperationException(
    FinancialCoreException
):
    """
    Operação matemática inválida.
    """
    pass
