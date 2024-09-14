from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarLockChairRsp(_message.Message):
    __slots__ = ("entity_id", "direction", "retcode", "chair_id", "position")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CHAIR_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    direction: int
    retcode: int
    chair_id: int
    position: _Vector_pb2.Vector
    def __init__(self, entity_id: _Optional[int] = ..., direction: _Optional[int] = ..., retcode: _Optional[int] = ..., chair_id: _Optional[int] = ..., position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
