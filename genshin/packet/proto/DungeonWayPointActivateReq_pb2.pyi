from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonWayPointActivateReq(_message.Message):
    __slots__ = ("way_point_id",)
    WAY_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    way_point_id: int
    def __init__(self, way_point_id: _Optional[int] = ...) -> None: ...
