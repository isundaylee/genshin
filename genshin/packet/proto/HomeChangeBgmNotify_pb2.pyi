from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeChangeBgmNotify(_message.Message):
    __slots__ = ("bgm_id",)
    BGM_ID_FIELD_NUMBER: _ClassVar[int]
    bgm_id: int
    def __init__(self, bgm_id: _Optional[int] = ...) -> None: ...
