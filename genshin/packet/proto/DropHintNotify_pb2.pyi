from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DropHintNotify(_message.Message):
    __slots__ = ("position", "item_id_list")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    position: _Vector_pb2.Vector
    item_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., item_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
