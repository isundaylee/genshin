from genshin.packet.proto import VehicleMember_pb2 as _VehicleMember_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import VehicleInteractType_pb2 as _VehicleInteractType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleInteractRsp(_message.Message):
    __slots__ = ("member", "GIICKAOFKDB", "retcode", "gadget_id", "entity_id", "vehicle_pos", "interact_type", "vehicle_rot")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    GIICKAOFKDB_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_POS_FIELD_NUMBER: _ClassVar[int]
    INTERACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ROT_FIELD_NUMBER: _ClassVar[int]
    member: _VehicleMember_pb2.VehicleMember
    GIICKAOFKDB: int
    retcode: int
    gadget_id: int
    entity_id: int
    vehicle_pos: _Vector_pb2.Vector
    interact_type: _VehicleInteractType_pb2.VehicleInteractType
    vehicle_rot: _Vector_pb2.Vector
    def __init__(self, member: _Optional[_Union[_VehicleMember_pb2.VehicleMember, _Mapping]] = ..., GIICKAOFKDB: _Optional[int] = ..., retcode: _Optional[int] = ..., gadget_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., vehicle_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., interact_type: _Optional[_Union[_VehicleInteractType_pb2.VehicleInteractType, str]] = ..., vehicle_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
