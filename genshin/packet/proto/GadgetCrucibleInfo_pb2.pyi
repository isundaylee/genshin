from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetCrucibleInfo(_message.Message):
    __slots__ = ("mp_play_id", "prepare_end_time")
    MP_PLAY_ID_FIELD_NUMBER: _ClassVar[int]
    PREPARE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    mp_play_id: int
    prepare_end_time: int
    def __init__(self, mp_play_id: _Optional[int] = ..., prepare_end_time: _Optional[int] = ...) -> None: ...
