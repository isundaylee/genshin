from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterWorldAreaReq(_message.Message):
    __slots__ = ("area_type", "area_id")
    AREA_TYPE_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    area_type: int
    area_id: int
    def __init__(self, area_type: _Optional[int] = ..., area_id: _Optional[int] = ...) -> None: ...
