from genshin.packet.proto import HomeBlockSubFieldData_pb2 as _HomeBlockSubFieldData_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBlockFieldData(_message.Message):
    __slots__ = ("sub_field_list", "furniture_id", "guid", "rot", "pos")
    SUB_FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    sub_field_list: _containers.RepeatedCompositeFieldContainer[_HomeBlockSubFieldData_pb2.HomeBlockSubFieldData]
    furniture_id: int
    guid: int
    rot: _Vector_pb2.Vector
    pos: _Vector_pb2.Vector
    def __init__(self, sub_field_list: _Optional[_Iterable[_Union[_HomeBlockSubFieldData_pb2.HomeBlockSubFieldData, _Mapping]]] = ..., furniture_id: _Optional[int] = ..., guid: _Optional[int] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
