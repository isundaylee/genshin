from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePointUnlockNotify(_message.Message):
    __slots__ = ("scene_id", "unhide_point_list", "point_list", "hide_point_list", "locked_point_list")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    UNHIDE_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    HIDE_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCKED_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    unhide_point_list: _containers.RepeatedScalarFieldContainer[int]
    point_list: _containers.RepeatedScalarFieldContainer[int]
    hide_point_list: _containers.RepeatedScalarFieldContainer[int]
    locked_point_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, scene_id: _Optional[int] = ..., unhide_point_list: _Optional[_Iterable[int]] = ..., point_list: _Optional[_Iterable[int]] = ..., hide_point_list: _Optional[_Iterable[int]] = ..., locked_point_list: _Optional[_Iterable[int]] = ...) -> None: ...
