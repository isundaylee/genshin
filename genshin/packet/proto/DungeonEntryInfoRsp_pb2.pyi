from genshin.packet.proto import DungeonEntryInfo_pb2 as _DungeonEntryInfo_pb2
from genshin.packet.proto import DungeonEntryPointInfo_pb2 as _DungeonEntryPointInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryInfoRsp(_message.Message):
    __slots__ = ("dungeon_entry_list", "dungeon_entry_point_list", "recommend_dungeon_id", "point_id", "retcode")
    DUNGEON_ENTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ENTRY_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    dungeon_entry_list: _containers.RepeatedCompositeFieldContainer[_DungeonEntryInfo_pb2.DungeonEntryInfo]
    dungeon_entry_point_list: _containers.RepeatedCompositeFieldContainer[_DungeonEntryPointInfo_pb2.DungeonEntryPointInfo]
    recommend_dungeon_id: int
    point_id: int
    retcode: int
    def __init__(self, dungeon_entry_list: _Optional[_Iterable[_Union[_DungeonEntryInfo_pb2.DungeonEntryInfo, _Mapping]]] = ..., dungeon_entry_point_list: _Optional[_Iterable[_Union[_DungeonEntryPointInfo_pb2.DungeonEntryPointInfo, _Mapping]]] = ..., recommend_dungeon_id: _Optional[int] = ..., point_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
