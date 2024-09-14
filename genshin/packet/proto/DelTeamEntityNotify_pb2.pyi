from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DelTeamEntityNotify(_message.Message):
    __slots__ = ("del_entity_id_list", "scene_id")
    DEL_ENTITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    del_entity_id_list: _containers.RepeatedScalarFieldContainer[int]
    scene_id: int
    def __init__(self, del_entity_id_list: _Optional[_Iterable[int]] = ..., scene_id: _Optional[int] = ...) -> None: ...
