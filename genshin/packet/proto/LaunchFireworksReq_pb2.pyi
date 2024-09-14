from genshin.packet.proto import FireworksLaunchSchemeData_pb2 as _FireworksLaunchSchemeData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchFireworksReq(_message.Message):
    __slots__ = ("scheme_data",)
    SCHEME_DATA_FIELD_NUMBER: _ClassVar[int]
    scheme_data: _FireworksLaunchSchemeData_pb2.FireworksLaunchSchemeData
    def __init__(self, scheme_data: _Optional[_Union[_FireworksLaunchSchemeData_pb2.FireworksLaunchSchemeData, _Mapping]] = ...) -> None: ...
