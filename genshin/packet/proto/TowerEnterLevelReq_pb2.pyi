from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerEnterLevelReq(_message.Message):
    __slots__ = ("enter_point_id",)
    ENTER_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    enter_point_id: int
    def __init__(self, enter_point_id: _Optional[int] = ...) -> None: ...
