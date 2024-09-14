from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HitTreeNotify(_message.Message):
    __slots__ = ("drop_pos", "tree_pos", "tree_type")
    DROP_POS_FIELD_NUMBER: _ClassVar[int]
    TREE_POS_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    drop_pos: _Vector_pb2.Vector
    tree_pos: _Vector_pb2.Vector
    tree_type: int
    def __init__(self, drop_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., tree_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., tree_type: _Optional[int] = ...) -> None: ...
