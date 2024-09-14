from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OneoffGatherPointDetectorData(_message.Message):
    __slots__ = ("config_id", "is_hint_valid", "hint_center_pos", "hint_radius", "material_id", "group_id", "is_all_collected")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    IS_HINT_VALID_FIELD_NUMBER: _ClassVar[int]
    HINT_CENTER_POS_FIELD_NUMBER: _ClassVar[int]
    HINT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ALL_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    is_hint_valid: bool
    hint_center_pos: _Vector_pb2.Vector
    hint_radius: int
    material_id: int
    group_id: int
    is_all_collected: bool
    def __init__(self, config_id: _Optional[int] = ..., is_hint_valid: bool = ..., hint_center_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., hint_radius: _Optional[int] = ..., material_id: _Optional[int] = ..., group_id: _Optional[int] = ..., is_all_collected: bool = ...) -> None: ...
