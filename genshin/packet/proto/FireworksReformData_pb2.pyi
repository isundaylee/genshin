from genshin.packet.proto import FireworksReformParam_pb2 as _FireworksReformParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireworksReformData(_message.Message):
    __slots__ = ("reform_param_list", "uk1", "id")
    REFORM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    UK1_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    reform_param_list: _containers.RepeatedCompositeFieldContainer[_FireworksReformParam_pb2.FireworksReformParam]
    uk1: _containers.RepeatedScalarFieldContainer[int]
    id: int
    def __init__(self, reform_param_list: _Optional[_Iterable[_Union[_FireworksReformParam_pb2.FireworksReformParam, _Mapping]]] = ..., uk1: _Optional[_Iterable[int]] = ..., id: _Optional[int] = ...) -> None: ...
