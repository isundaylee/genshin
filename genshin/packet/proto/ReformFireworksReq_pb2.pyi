from genshin.packet.proto import FireworksReformData_pb2 as _FireworksReformData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReformFireworksReq(_message.Message):
    __slots__ = ("fireworks_reform_data",)
    FIREWORKS_REFORM_DATA_FIELD_NUMBER: _ClassVar[int]
    fireworks_reform_data: _FireworksReformData_pb2.FireworksReformData
    def __init__(self, fireworks_reform_data: _Optional[_Union[_FireworksReformData_pb2.FireworksReformData, _Mapping]] = ...) -> None: ...
