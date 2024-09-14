from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TryEnterHomeRsp(_message.Message):
    __slots__ = ("retcode", "param_list", "target_uid")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    param_list: _containers.RepeatedScalarFieldContainer[int]
    target_uid: int
    def __init__(self, retcode: _Optional[int] = ..., param_list: _Optional[_Iterable[int]] = ..., target_uid: _Optional[int] = ...) -> None: ...
