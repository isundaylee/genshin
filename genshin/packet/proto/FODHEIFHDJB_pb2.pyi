from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FODHEIFHDJB(_message.Message):
    __slots__ = ("DHKJKGIGJDG", "BNHEAFCGIJM", "costume_id", "avatar_id")
    DHKJKGIGJDG_FIELD_NUMBER: _ClassVar[int]
    BNHEAFCGIJM_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    DHKJKGIGJDG: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    BNHEAFCGIJM: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    costume_id: int
    avatar_id: int
    def __init__(self, DHKJKGIGJDG: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., BNHEAFCGIJM: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., costume_id: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
