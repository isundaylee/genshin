from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateVehicleRsp(_message.Message):
    __slots__ = ("entity_id", "retcode", "vehicle_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    retcode: int
    vehicle_id: int
    def __init__(self, entity_id: _Optional[int] = ..., retcode: _Optional[int] = ..., vehicle_id: _Optional[int] = ...) -> None: ...
