from __future__ import annotations

from typing import get_type_hints
from uuid import UUID

from app.domain.common.financial_core.execution.snapshot import (
    SnapshotRepository,
)


def test_snapshot_repository_is_abstract() -> None:

    assert issubclass(
        SnapshotRepository,
        object,
    )

    assert hasattr(
        SnapshotRepository,
        "save",
    )

    assert hasattr(
        SnapshotRepository,
        "load",
    )


def test_snapshot_repository_load_signature() -> None:

    annotations = get_type_hints(
        SnapshotRepository.load,
    )

    assert annotations["execution_id"] is UUID
