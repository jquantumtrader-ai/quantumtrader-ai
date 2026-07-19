from enum import Enum


class ExecutionStatus(str, Enum):
    """
    Estados possíveis de uma execução.
    """

    CREATED = "CREATED"

    PENDING = "PENDING"

    PARTIAL = "PARTIAL"

    FILLED = "FILLED"

    REJECTED = "REJECTED"

    CANCELLED = "CANCELLED"
