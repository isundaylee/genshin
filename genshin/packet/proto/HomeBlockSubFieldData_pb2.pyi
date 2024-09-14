from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBlockSubFieldData(_message.Message):
    __slots__ = ("rot", "pos")
    ROT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    rot: _Vector_pb2.Vector
    pos: _Vector_pb2.Vector
    def __init__(self, rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
