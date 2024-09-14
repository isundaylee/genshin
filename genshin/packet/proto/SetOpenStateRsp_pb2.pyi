from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetOpenStateRsp(_message.Message):
    __slots__ = ("key", "retcode", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    retcode: int
    value: int
    def __init__(self, key: _Optional[int] = ..., retcode: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
