from genshin.packet.proto import FurnitureMakeData_pb2 as _FurnitureMakeData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeSlot(_message.Message):
    __slots__ = ("furniture_make_data_list",)
    FURNITURE_MAKE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    furniture_make_data_list: _containers.RepeatedCompositeFieldContainer[_FurnitureMakeData_pb2.FurnitureMakeData]
    def __init__(self, furniture_make_data_list: _Optional[_Iterable[_Union[_FurnitureMakeData_pb2.FurnitureMakeData, _Mapping]]] = ...) -> None: ...
