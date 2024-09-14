from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerAllDataReq(_message.Message):
    __slots__ = ("is_interact",)
    IS_INTERACT_FIELD_NUMBER: _ClassVar[int]
    is_interact: bool
    def __init__(self, is_interact: bool = ...) -> None: ...
