from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FleurFairMusicGameStartReq(_message.Message):
    __slots__ = ("music_basic_id",)
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    music_basic_id: int
    def __init__(self, music_basic_id: _Optional[int] = ...) -> None: ...
