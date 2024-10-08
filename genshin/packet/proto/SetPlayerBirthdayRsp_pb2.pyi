from genshin.packet.proto import Birthday_pb2 as _Birthday_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerBirthdayRsp(_message.Message):
    __slots__ = ("birthday", "retcode")
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    birthday: _Birthday_pb2.Birthday
    retcode: int
    def __init__(self, birthday: _Optional[_Union[_Birthday_pb2.Birthday, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
