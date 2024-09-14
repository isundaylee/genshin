from genshin.packet.proto import HomeFurnitureData_pb2 as _HomeFurnitureData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeFurnitureGroupData(_message.Message):
    __slots__ = ("virtual_furniure_list", "group_furniture_index")
    VIRTUAL_FURNIURE_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_FURNITURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    virtual_furniure_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureData_pb2.HomeFurnitureData]
    group_furniture_index: int
    def __init__(self, virtual_furniure_list: _Optional[_Iterable[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]]] = ..., group_furniture_index: _Optional[int] = ...) -> None: ...
