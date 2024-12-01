from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NPNFLLGHMKN(_message.Message):
    __slots__ = ("level", "exp")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    level: int
    exp: int
    def __init__(self, level: _Optional[int] = ..., exp: _Optional[int] = ...) -> None: ...
