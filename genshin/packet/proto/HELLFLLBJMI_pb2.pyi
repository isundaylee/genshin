from genshin.packet.proto import KHBDLLKPLFG_pb2 as _KHBDLLKPLFG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HELLFLLBJMI(_message.Message):
    __slots__ = ("BBPGIJFJHEN", "avatar_id", "avatar_type", "COOHEMDONKJ", "costume_id")
    BBPGIJFJHEN_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COOHEMDONKJ_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    BBPGIJFJHEN: int
    avatar_id: int
    avatar_type: _KHBDLLKPLFG_pb2.KHBDLLKPLFG
    COOHEMDONKJ: int
    costume_id: int
    def __init__(self, BBPGIJFJHEN: _Optional[int] = ..., avatar_id: _Optional[int] = ..., avatar_type: _Optional[_Union[_KHBDLLKPLFG_pb2.KHBDLLKPLFG, str]] = ..., COOHEMDONKJ: _Optional[int] = ..., costume_id: _Optional[int] = ...) -> None: ...
