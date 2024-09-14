from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuyResinRsp(_message.Message):
    __slots__ = ("retcode", "cur_value")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CUR_VALUE_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    cur_value: int
    def __init__(self, retcode: _Optional[int] = ..., cur_value: _Optional[int] = ...) -> None: ...
