from genshin.packet.proto import DungeonEnterPosInfo_pb2 as _DungeonEnterPosInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerEnterDungeonReq(_message.Message):
    __slots__ = ("enter_pos_info", "LLCOCJHJBME", "dungeon_id", "point_id")
    ENTER_POS_INFO_FIELD_NUMBER: _ClassVar[int]
    LLCOCJHJBME_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    enter_pos_info: _DungeonEnterPosInfo_pb2.DungeonEnterPosInfo
    LLCOCJHJBME: bool
    dungeon_id: int
    point_id: int
    def __init__(self, enter_pos_info: _Optional[_Union[_DungeonEnterPosInfo_pb2.DungeonEnterPosInfo, _Mapping]] = ..., LLCOCJHJBME: bool = ..., dungeon_id: _Optional[int] = ..., point_id: _Optional[int] = ...) -> None: ...
