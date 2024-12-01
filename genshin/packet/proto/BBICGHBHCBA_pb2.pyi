from genshin.packet.proto import BHJBDLJAKMG_pb2 as _BHJBDLJAKMG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BBICGHBHCBA(_message.Message):
    __slots__ = ("avatar_type", "avatar_id", "costume_id")
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_type: _BHJBDLJAKMG_pb2.BHJBDLJAKMG
    avatar_id: int
    costume_id: int
    def __init__(self, avatar_type: _Optional[_Union[_BHJBDLJAKMG_pb2.BHJBDLJAKMG, str]] = ..., avatar_id: _Optional[int] = ..., costume_id: _Optional[int] = ...) -> None: ...
