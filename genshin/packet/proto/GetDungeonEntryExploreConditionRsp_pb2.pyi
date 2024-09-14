from genshin.packet.proto import DungeonEntryCond_pb2 as _DungeonEntryCond_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDungeonEntryExploreConditionRsp(_message.Message):
    __slots__ = ("dungeon_entry_cond", "retcode")
    DUNGEON_ENTRY_COND_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    dungeon_entry_cond: _DungeonEntryCond_pb2.DungeonEntryCond
    retcode: int
    def __init__(self, dungeon_entry_cond: _Optional[_Union[_DungeonEntryCond_pb2.DungeonEntryCond, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
