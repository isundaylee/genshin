from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModifierDurability(_message.Message):
    __slots__ = ("reduce_ratio", "remaining_durability")
    REDUCE_RATIO_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    reduce_ratio: float
    remaining_durability: float
    def __init__(self, reduce_ratio: _Optional[float] = ..., remaining_durability: _Optional[float] = ...) -> None: ...
