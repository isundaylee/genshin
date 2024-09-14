from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BargainSnapshot(_message.Message):
    __slots__ = ("IOCNPJJNHLD", "BALOPACHCDB", "cur_mood", "bargain_id")
    IOCNPJJNHLD_FIELD_NUMBER: _ClassVar[int]
    BALOPACHCDB_FIELD_NUMBER: _ClassVar[int]
    CUR_MOOD_FIELD_NUMBER: _ClassVar[int]
    BARGAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IOCNPJJNHLD: int
    BALOPACHCDB: int
    cur_mood: int
    bargain_id: int
    def __init__(self, IOCNPJJNHLD: _Optional[int] = ..., BALOPACHCDB: _Optional[int] = ..., cur_mood: _Optional[int] = ..., bargain_id: _Optional[int] = ...) -> None: ...
