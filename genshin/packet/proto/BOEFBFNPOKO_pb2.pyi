from genshin.packet.proto import KHBDLLKPLFG_pb2 as _KHBDLLKPLFG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BOEFBFNPOKO(_message.Message):
    __slots__ = ("costume_id", "avatar_id", "CFFMDKNINHD", "avatar_type")
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    CFFMDKNINHD_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    costume_id: int
    avatar_id: int
    CFFMDKNINHD: int
    avatar_type: _KHBDLLKPLFG_pb2.KHBDLLKPLFG
    def __init__(self, costume_id: _Optional[int] = ..., avatar_id: _Optional[int] = ..., CFFMDKNINHD: _Optional[int] = ..., avatar_type: _Optional[_Union[_KHBDLLKPLFG_pb2.KHBDLLKPLFG, str]] = ...) -> None: ...
