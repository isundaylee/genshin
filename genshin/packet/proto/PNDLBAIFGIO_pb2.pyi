from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PNDLBAIFGIO(_message.Message):
    __slots__ = ("NKANJIJNIMC", "DMJODFMIIDG", "BILEKHIENED")
    NKANJIJNIMC_FIELD_NUMBER: _ClassVar[int]
    DMJODFMIIDG_FIELD_NUMBER: _ClassVar[int]
    BILEKHIENED_FIELD_NUMBER: _ClassVar[int]
    NKANJIJNIMC: str
    DMJODFMIIDG: int
    BILEKHIENED: int
    def __init__(self, NKANJIJNIMC: _Optional[str] = ..., DMJODFMIIDG: _Optional[int] = ..., BILEKHIENED: _Optional[int] = ...) -> None: ...
