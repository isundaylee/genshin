from genshin.packet.proto import ChallengeBrief_pb2 as _ChallengeBrief_pb2
from genshin.packet.proto import CustomDungeonFinishType_pb2 as _CustomDungeonFinishType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomDungeonResultInfo(_message.Message):
    __slots__ = ("child_challenge_list", "got_coin_num", "FOLIKAAIKIE", "GBLHFAEONKM", "finish_type", "time_cost", "LHNFIIEJBEM", "dungeon_guid")
    CHILD_CHALLENGE_LIST_FIELD_NUMBER: _ClassVar[int]
    GOT_COIN_NUM_FIELD_NUMBER: _ClassVar[int]
    FOLIKAAIKIE_FIELD_NUMBER: _ClassVar[int]
    GBLHFAEONKM_FIELD_NUMBER: _ClassVar[int]
    FINISH_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_COST_FIELD_NUMBER: _ClassVar[int]
    LHNFIIEJBEM_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_GUID_FIELD_NUMBER: _ClassVar[int]
    child_challenge_list: _containers.RepeatedCompositeFieldContainer[_ChallengeBrief_pb2.ChallengeBrief]
    got_coin_num: int
    FOLIKAAIKIE: bool
    GBLHFAEONKM: bool
    finish_type: _CustomDungeonFinishType_pb2.CustomDungeonFinishType
    time_cost: int
    LHNFIIEJBEM: bool
    dungeon_guid: int
    def __init__(self, child_challenge_list: _Optional[_Iterable[_Union[_ChallengeBrief_pb2.ChallengeBrief, _Mapping]]] = ..., got_coin_num: _Optional[int] = ..., FOLIKAAIKIE: bool = ..., GBLHFAEONKM: bool = ..., finish_type: _Optional[_Union[_CustomDungeonFinishType_pb2.CustomDungeonFinishType, str]] = ..., time_cost: _Optional[int] = ..., LHNFIIEJBEM: bool = ..., dungeon_guid: _Optional[int] = ...) -> None: ...
