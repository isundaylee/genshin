from genshin.packet.proto import TowerLevelStarCondData_pb2 as _TowerLevelStarCondData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerLevelStarCondNotify(_message.Message):
    __slots__ = ("cond_data_list", "floor_id", "level_index")
    COND_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    cond_data_list: _containers.RepeatedCompositeFieldContainer[_TowerLevelStarCondData_pb2.TowerLevelStarCondData]
    floor_id: int
    level_index: int
    def __init__(self, cond_data_list: _Optional[_Iterable[_Union[_TowerLevelStarCondData_pb2.TowerLevelStarCondData, _Mapping]]] = ..., floor_id: _Optional[int] = ..., level_index: _Optional[int] = ...) -> None: ...
