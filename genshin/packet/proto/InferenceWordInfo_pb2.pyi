from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InferenceWordInfo(_message.Message):
    __slots__ = ("DHBPEBDBMNK", "CAJHCPIPBOO", "word_id", "unlock_by_word_id", "ENFPKOPNHKK")
    DHBPEBDBMNK_FIELD_NUMBER: _ClassVar[int]
    CAJHCPIPBOO_FIELD_NUMBER: _ClassVar[int]
    WORD_ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_BY_WORD_ID_FIELD_NUMBER: _ClassVar[int]
    ENFPKOPNHKK_FIELD_NUMBER: _ClassVar[int]
    DHBPEBDBMNK: bool
    CAJHCPIPBOO: bool
    word_id: int
    unlock_by_word_id: int
    ENFPKOPNHKK: bool
    def __init__(self, DHBPEBDBMNK: bool = ..., CAJHCPIPBOO: bool = ..., word_id: _Optional[int] = ..., unlock_by_word_id: _Optional[int] = ..., ENFPKOPNHKK: bool = ...) -> None: ...
