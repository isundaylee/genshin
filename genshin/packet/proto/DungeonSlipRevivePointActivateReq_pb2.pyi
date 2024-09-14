from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSlipRevivePointActivateReq(_message.Message):
    __slots__ = ("slip_revive_point_id",)
    SLIP_REVIVE_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    slip_revive_point_id: int
    def __init__(self, slip_revive_point_id: _Optional[int] = ...) -> None: ...
