from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkyCrystalDetectorData(_message.Message):
    __slots__ = ("group_id", "config_id", "hint_center_pos", "is_hint_valid")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    HINT_CENTER_POS_FIELD_NUMBER: _ClassVar[int]
    IS_HINT_VALID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    config_id: int
    hint_center_pos: _Vector_pb2.Vector
    is_hint_valid: bool
    def __init__(self, group_id: _Optional[int] = ..., config_id: _Optional[int] = ..., hint_center_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., is_hint_valid: bool = ...) -> None: ...
