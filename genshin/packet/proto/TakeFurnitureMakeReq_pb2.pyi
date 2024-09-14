from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeFurnitureMakeReq(_message.Message):
    __slots__ = ("index", "is_fast_finish", "make_id")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_FAST_FINISH_FIELD_NUMBER: _ClassVar[int]
    MAKE_ID_FIELD_NUMBER: _ClassVar[int]
    index: int
    is_fast_finish: bool
    make_id: int
    def __init__(self, index: _Optional[int] = ..., is_fast_finish: bool = ..., make_id: _Optional[int] = ...) -> None: ...
