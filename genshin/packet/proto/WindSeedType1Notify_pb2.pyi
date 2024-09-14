from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WindSeedType1Notify(_message.Message):
    __slots__ = ("config_id", "payload")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    payload: bytes
    def __init__(self, config_id: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...
