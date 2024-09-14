from genshin.packet.proto import VehicleInteractType_pb2 as _VehicleInteractType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleInteractReq(_message.Message):
    __slots__ = ("pos", "entity_id", "EILHBJJEPOK", "interact_type")
    POS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EILHBJJEPOK_FIELD_NUMBER: _ClassVar[int]
    INTERACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    pos: int
    entity_id: int
    EILHBJJEPOK: bool
    interact_type: _VehicleInteractType_pb2.VehicleInteractType
    def __init__(self, pos: _Optional[int] = ..., entity_id: _Optional[int] = ..., EILHBJJEPOK: bool = ..., interact_type: _Optional[_Union[_VehicleInteractType_pb2.VehicleInteractType, str]] = ...) -> None: ...
