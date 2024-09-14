from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EntityEnvironmentInfo(_message.Message):
    __slots__ = ("json_climate_type", "climate_area_id")
    JSON_CLIMATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    json_climate_type: int
    climate_area_id: int
    def __init__(self, json_climate_type: _Optional[int] = ..., climate_area_id: _Optional[int] = ...) -> None: ...
