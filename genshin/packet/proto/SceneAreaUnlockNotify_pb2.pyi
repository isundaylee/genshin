from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAreaUnlockNotify(_message.Message):
    __slots__ = ("area_list", "scene_id")
    AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    area_list: _containers.RepeatedScalarFieldContainer[int]
    scene_id: int
    def __init__(self, area_list: _Optional[_Iterable[int]] = ..., scene_id: _Optional[int] = ...) -> None: ...
