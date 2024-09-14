from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerLocationInfo(_message.Message):
    __slots__ = ("pos", "uid", "rot", "KJAEPLIIAIH")
    POS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    KJAEPLIIAIH_FIELD_NUMBER: _ClassVar[int]
    pos: _Vector_pb2.Vector
    uid: int
    rot: _Vector_pb2.Vector
    KJAEPLIIAIH: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., uid: _Optional[int] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., KJAEPLIIAIH: _Optional[_Iterable[int]] = ...) -> None: ...
