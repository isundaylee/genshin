from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRTTInfo(_message.Message):
    __slots__ = ("NCCPPHNNPBF", "OAFKLBDFLJG")
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    OAFKLBDFLJG_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF: int
    OAFKLBDFLJG: int
    def __init__(self, NCCPPHNNPBF: _Optional[int] = ..., OAFKLBDFLJG: _Optional[int] = ...) -> None: ...
