from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BlockInfo(_message.Message):
    __slots__ = ("block_id", "GFKFJJOADMH", "NEHMEMLKIPP", "GLAFBCFFAEG")
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    GFKFJJOADMH_FIELD_NUMBER: _ClassVar[int]
    NEHMEMLKIPP_FIELD_NUMBER: _ClassVar[int]
    GLAFBCFFAEG_FIELD_NUMBER: _ClassVar[int]
    block_id: int
    GFKFJJOADMH: int
    NEHMEMLKIPP: bytes
    GLAFBCFFAEG: bool
    def __init__(self, block_id: _Optional[int] = ..., GFKFJJOADMH: _Optional[int] = ..., NEHMEMLKIPP: _Optional[bytes] = ..., GLAFBCFFAEG: bool = ...) -> None: ...
