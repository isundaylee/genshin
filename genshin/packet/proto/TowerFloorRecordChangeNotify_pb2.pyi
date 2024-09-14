from genshin.packet.proto import TowerFloorRecord_pb2 as _TowerFloorRecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerFloorRecordChangeNotify(_message.Message):
    __slots__ = ("is_finished_entrance_floor", "tower_floor_record_list")
    IS_FINISHED_ENTRANCE_FLOOR_FIELD_NUMBER: _ClassVar[int]
    TOWER_FLOOR_RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    is_finished_entrance_floor: bool
    tower_floor_record_list: _containers.RepeatedCompositeFieldContainer[_TowerFloorRecord_pb2.TowerFloorRecord]
    def __init__(self, is_finished_entrance_floor: bool = ..., tower_floor_record_list: _Optional[_Iterable[_Union[_TowerFloorRecord_pb2.TowerFloorRecord, _Mapping]]] = ...) -> None: ...
