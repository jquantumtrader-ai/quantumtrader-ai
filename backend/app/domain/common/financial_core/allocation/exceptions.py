"""
Exceções relacionadas ao sistema de alocação monetária.
"""


class AllocationError(Exception):
    """
    Exceção base para erros de alocação.
    """


class InvalidAllocationRatioError(AllocationError):
    """
    Lançada quando os pesos informados são inválidos.
    """


class EmptyAllocationError(AllocationError):
    """
    Lançada quando nenhuma razão é informada.
    """
