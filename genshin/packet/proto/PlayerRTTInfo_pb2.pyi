from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRTTInfo(_message.Message):
    __slots__ = ("rtt", "uid")
    RTT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    rtt: int
    uid: int
    def __init__(self, rtt: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...
