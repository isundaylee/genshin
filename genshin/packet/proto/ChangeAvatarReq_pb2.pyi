from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeAvatarReq(_message.Message):
    __slots__ = ("move_pos", "skill_id", "IMPLCNKLFED", "is_move", "guid")
    MOVE_POS_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IMPLCNKLFED_FIELD_NUMBER: _ClassVar[int]
    IS_MOVE_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    move_pos: _Vector_pb2.Vector
    skill_id: int
    IMPLCNKLFED: bool
    is_move: bool
    guid: int
    def __init__(self, move_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., skill_id: _Optional[int] = ..., IMPLCNKLFED: bool = ..., is_move: bool = ..., guid: _Optional[int] = ...) -> None: ...
