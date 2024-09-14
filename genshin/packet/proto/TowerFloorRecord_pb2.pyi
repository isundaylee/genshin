from genshin.packet.proto import TowerLevelRecord_pb2 as _TowerLevelRecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerFloorRecord(_message.Message):
    __slots__ = ("passed_level_map", "passed_level_record_list", "floor_star_reward_progress", "floor_id")
    class PassedLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PASSED_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    PASSED_LEVEL_RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    FLOOR_STAR_REWARD_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    passed_level_map: _containers.ScalarMap[int, int]
    passed_level_record_list: _containers.RepeatedCompositeFieldContainer[_TowerLevelRecord_pb2.TowerLevelRecord]
    floor_star_reward_progress: int
    floor_id: int
    def __init__(self, passed_level_map: _Optional[_Mapping[int, int]] = ..., passed_level_record_list: _Optional[_Iterable[_Union[_TowerLevelRecord_pb2.TowerLevelRecord, _Mapping]]] = ..., floor_star_reward_progress: _Optional[int] = ..., floor_id: _Optional[int] = ...) -> None: ...
