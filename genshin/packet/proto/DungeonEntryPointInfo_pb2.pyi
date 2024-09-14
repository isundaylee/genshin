from genshin.packet.proto import DungeonEntryInfo_pb2 as _DungeonEntryInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryPointInfo(_message.Message):
    __slots__ = ("dungeon_entry_list", "point_id", "recommend_dungeon_id", "scene_id")
    DUNGEON_ENTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    dungeon_entry_list: _containers.RepeatedCompositeFieldContainer[_DungeonEntryInfo_pb2.DungeonEntryInfo]
    point_id: int
    recommend_dungeon_id: int
    scene_id: int
    def __init__(self, dungeon_entry_list: _Optional[_Iterable[_Union[_DungeonEntryInfo_pb2.DungeonEntryInfo, _Mapping]]] = ..., point_id: _Optional[int] = ..., recommend_dungeon_id: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
