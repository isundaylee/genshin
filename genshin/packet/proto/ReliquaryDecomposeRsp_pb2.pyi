from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReliquaryDecomposeRsp(_message.Message):
    __slots__ = ("guid_list", "retcode")
    GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    guid_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, guid_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
