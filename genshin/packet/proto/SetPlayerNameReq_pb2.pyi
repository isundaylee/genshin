from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerNameReq(_message.Message):
    __slots__ = ("nick_name",)
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    nick_name: str
    def __init__(self, nick_name: _Optional[str] = ...) -> None: ...
