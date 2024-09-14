from genshin.packet.proto import CodexType_pb2 as _CodexType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CodexDataUpdateNotify(_message.Message):
    __slots__ = ("id", "type", "weapon_max_promote_level")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_MAX_PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: _CodexType_pb2.CodexType
    weapon_max_promote_level: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[_CodexType_pb2.CodexType, str]] = ..., weapon_max_promote_level: _Optional[int] = ...) -> None: ...
