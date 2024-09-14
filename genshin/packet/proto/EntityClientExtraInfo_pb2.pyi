from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityClientExtraInfo(_message.Message):
    __slots__ = ("FFIOLDKCHCK",)
    FFIOLDKCHCK_FIELD_NUMBER: _ClassVar[int]
    FFIOLDKCHCK: _Vector_pb2.Vector
    def __init__(self, FFIOLDKCHCK: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
