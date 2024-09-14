from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarSitDownNotify(_message.Message):
    __slots__ = ("chair_id", "direction", "position", "entity_id")
    CHAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    chair_id: int
    direction: int
    position: _Vector_pb2.Vector
    entity_id: int
    def __init__(self, chair_id: _Optional[int] = ..., direction: _Optional[int] = ..., position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...
