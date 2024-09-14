from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarLockChairReq(_message.Message):
    __slots__ = ("position", "chair_id", "direction")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    CHAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    position: _Vector_pb2.Vector
    chair_id: int
    direction: int
    def __init__(self, position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., chair_id: _Optional[int] = ..., direction: _Optional[int] = ...) -> None: ...
