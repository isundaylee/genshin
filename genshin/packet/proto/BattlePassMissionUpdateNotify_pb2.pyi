from genshin.packet.proto import BattlePassMission_pb2 as _BattlePassMission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassMissionUpdateNotify(_message.Message):
    __slots__ = ("mission_list",)
    MISSION_LIST_FIELD_NUMBER: _ClassVar[int]
    mission_list: _containers.RepeatedCompositeFieldContainer[_BattlePassMission_pb2.BattlePassMission]
    def __init__(self, mission_list: _Optional[_Iterable[_Union[_BattlePassMission_pb2.BattlePassMission, _Mapping]]] = ...) -> None: ...
