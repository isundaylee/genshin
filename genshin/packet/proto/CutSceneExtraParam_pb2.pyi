from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CutSceneExtraParam(_message.Message):
    __slots__ = ("detail_param_list",)
    DETAIL_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    detail_param_list: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, detail_param_list: _Optional[_Iterable[float]] = ...) -> None: ...
