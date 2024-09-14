from genshin.packet.proto import DailyDungeonEntryInfo_pb2 as _DailyDungeonEntryInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDailyDungeonEntryInfoRsp(_message.Message):
    __slots__ = ("daily_dungeon_info_list", "retcode")
    DAILY_DUNGEON_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    daily_dungeon_info_list: _containers.RepeatedCompositeFieldContainer[_DailyDungeonEntryInfo_pb2.DailyDungeonEntryInfo]
    retcode: int
    def __init__(self, daily_dungeon_info_list: _Optional[_Iterable[_Union[_DailyDungeonEntryInfo_pb2.DailyDungeonEntryInfo, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
