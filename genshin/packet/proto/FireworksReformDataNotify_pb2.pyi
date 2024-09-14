from genshin.packet.proto import FireworksReformData_pb2 as _FireworksReformData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireworksReformDataNotify(_message.Message):
    __slots__ = ("uk1", "fireworks_reform_data_list")
    UK1_FIELD_NUMBER: _ClassVar[int]
    FIREWORKS_REFORM_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    uk1: int
    fireworks_reform_data_list: _containers.RepeatedCompositeFieldContainer[_FireworksReformData_pb2.FireworksReformData]
    def __init__(self, uk1: _Optional[int] = ..., fireworks_reform_data_list: _Optional[_Iterable[_Union[_FireworksReformData_pb2.FireworksReformData, _Mapping]]] = ...) -> None: ...
