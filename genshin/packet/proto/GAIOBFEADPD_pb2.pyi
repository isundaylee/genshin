from genshin.packet.proto import OBDLODPCEJI_pb2 as _OBDLODPCEJI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GAIOBFEADPD(_message.Message):
    __slots__ = ("avatar_type", "ECHJDBKMIGG", "costume_id")
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ECHJDBKMIGG_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_type: _OBDLODPCEJI_pb2.OBDLODPCEJI
    ECHJDBKMIGG: int
    costume_id: int
    def __init__(self, avatar_type: _Optional[_Union[_OBDLODPCEJI_pb2.OBDLODPCEJI, str]] = ..., ECHJDBKMIGG: _Optional[int] = ..., costume_id: _Optional[int] = ...) -> None: ...
