from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarDieAnimationEndReq(_message.Message):
    __slots__ = ("reborn_pos", "die_guid", "skill_id")
    REBORN_POS_FIELD_NUMBER: _ClassVar[int]
    DIE_GUID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    reborn_pos: _Vector_pb2.Vector
    die_guid: int
    skill_id: int
    def __init__(self, reborn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., die_guid: _Optional[int] = ..., skill_id: _Optional[int] = ...) -> None: ...
