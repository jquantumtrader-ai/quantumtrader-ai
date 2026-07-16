class CurrencyMismatchError(Exception):
    """
    Exceção lançada quando operações
    envolvem moedas diferentes.
    """

    def __init__(
        self,
        message: str = "Moedas incompatíveis para operação."
    ) -> None:
        super().__init__(message)
