from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StartCoopPointReq(_message.Message):
    __slots__ = ("coop_point",)
    COOP_POINT_FIELD_NUMBER: _ClassVar[int]
    coop_point: int
    def __init__(self, coop_point: _Optional[int] = ...) -> None: ...
