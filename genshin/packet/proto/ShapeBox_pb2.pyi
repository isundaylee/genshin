from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShapeBox(_message.Message):
    __slots__ = ("center", "extents", "axis0", "axis1", "axis4")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    EXTENTS_FIELD_NUMBER: _ClassVar[int]
    AXIS0_FIELD_NUMBER: _ClassVar[int]
    AXIS1_FIELD_NUMBER: _ClassVar[int]
    AXIS4_FIELD_NUMBER: _ClassVar[int]
    center: _Vector_pb2.Vector
    extents: _Vector_pb2.Vector
    axis0: _Vector_pb2.Vector
    axis1: _Vector_pb2.Vector
    axis4: _Vector_pb2.Vector
    def __init__(self, center: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., extents: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., axis0: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., axis1: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., axis4: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
