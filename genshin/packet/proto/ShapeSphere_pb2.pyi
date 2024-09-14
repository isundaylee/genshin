from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShapeSphere(_message.Message):
    __slots__ = ("center", "radius")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    center: _Vector_pb2.Vector
    radius: float
    def __init__(self, center: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., radius: _Optional[float] = ...) -> None: ...
