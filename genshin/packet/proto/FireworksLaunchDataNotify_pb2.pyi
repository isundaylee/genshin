from genshin.packet.proto import FireworksLaunchSchemeData_pb2 as _FireworksLaunchSchemeData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireworksLaunchDataNotify(_message.Message):
    __slots__ = ("scheme_data_list", "last_use_scheme_id")
    SCHEME_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    LAST_USE_SCHEME_ID_FIELD_NUMBER: _ClassVar[int]
    scheme_data_list: _containers.RepeatedCompositeFieldContainer[_FireworksLaunchSchemeData_pb2.FireworksLaunchSchemeData]
    last_use_scheme_id: int
    def __init__(self, scheme_data_list: _Optional[_Iterable[_Union[_FireworksLaunchSchemeData_pb2.FireworksLaunchSchemeData, _Mapping]]] = ..., last_use_scheme_id: _Optional[int] = ...) -> None: ...
