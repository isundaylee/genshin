from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")


def assert_not_none(v: T | None) -> T:
    assert v is not None
    return v
