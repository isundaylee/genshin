from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerNameRsp(_message.Message):
    __slots__ = ("nick_name", "retcode")
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    nick_name: str
    retcode: int
    def __init__(self, nick_name: _Optional[str] = ..., retcode: _Optional[int] = ...) -> None: ...
