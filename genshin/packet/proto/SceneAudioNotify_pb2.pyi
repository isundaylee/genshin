from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAudioNotify(_message.Message):
    __slots__ = ("param3", "param2", "source_uid", "param1", "type")
    PARAM3_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UID_FIELD_NUMBER: _ClassVar[int]
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    param3: _containers.RepeatedScalarFieldContainer[str]
    param2: _containers.RepeatedScalarFieldContainer[float]
    source_uid: int
    param1: _containers.RepeatedScalarFieldContainer[int]
    type: int
    def __init__(self, param3: _Optional[_Iterable[str]] = ..., param2: _Optional[_Iterable[float]] = ..., source_uid: _Optional[int] = ..., param1: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ...) -> None: ...
