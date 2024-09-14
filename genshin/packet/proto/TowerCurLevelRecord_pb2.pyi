from genshin.packet.proto import TowerTeam_pb2 as _TowerTeam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerCurLevelRecord(_message.Message):
    __slots__ = ("cur_floor_id", "is_empty", "tower_team_list", "buff_id_list", "cur_level_index", "is_upper_part")
    CUR_FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
    TOWER_TEAM_LIST_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_UPPER_PART_FIELD_NUMBER: _ClassVar[int]
    cur_floor_id: int
    is_empty: bool
    tower_team_list: _containers.RepeatedCompositeFieldContainer[_TowerTeam_pb2.TowerTeam]
    buff_id_list: _containers.RepeatedScalarFieldContainer[int]
    cur_level_index: int
    is_upper_part: bool
    def __init__(self, cur_floor_id: _Optional[int] = ..., is_empty: bool = ..., tower_team_list: _Optional[_Iterable[_Union[_TowerTeam_pb2.TowerTeam, _Mapping]]] = ..., buff_id_list: _Optional[_Iterable[int]] = ..., cur_level_index: _Optional[int] = ..., is_upper_part: bool = ...) -> None: ...
