from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CurVehicleInfo(_message.Message):
    __slots__ = ("entity_id", "pos", "gadget_id", "vehicle_pos", "GIICKAOFKDB", "vehicle_rot")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_POS_FIELD_NUMBER: _ClassVar[int]
    GIICKAOFKDB_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ROT_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    pos: int
    gadget_id: int
    vehicle_pos: _Vector_pb2.Vector
    GIICKAOFKDB: int
    vehicle_rot: _Vector_pb2.Vector
    def __init__(self, entity_id: _Optional[int] = ..., pos: _Optional[int] = ..., gadget_id: _Optional[int] = ..., vehicle_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., GIICKAOFKDB: _Optional[int] = ..., vehicle_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
