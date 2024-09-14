from genshin.packet.proto import TowerTeam_pb2 as _TowerTeam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerTeamSelectReq(_message.Message):
    __slots__ = ("floor_id", "tower_team_list")
    FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    TOWER_TEAM_LIST_FIELD_NUMBER: _ClassVar[int]
    floor_id: int
    tower_team_list: _containers.RepeatedCompositeFieldContainer[_TowerTeam_pb2.TowerTeam]
    def __init__(self, floor_id: _Optional[int] = ..., tower_team_list: _Optional[_Iterable[_Union[_TowerTeam_pb2.TowerTeam, _Mapping]]] = ...) -> None: ...
