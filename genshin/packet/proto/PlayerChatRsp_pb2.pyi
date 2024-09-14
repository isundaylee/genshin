from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerChatRsp(_message.Message):
    __slots__ = ("chat_forbidden_endtime", "retcode")
    CHAT_FORBIDDEN_ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    chat_forbidden_endtime: int
    retcode: int
    def __init__(self, chat_forbidden_endtime: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
