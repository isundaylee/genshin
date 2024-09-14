from genshin.packet.proto import FireworksLaunchParamType_pb2 as _FireworksLaunchParamType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireworksLaunchParam(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _FireworksLaunchParamType_pb2.FireworksLaunchParamType
    value: int
    def __init__(self, type: _Optional[_Union[_FireworksLaunchParamType_pb2.FireworksLaunchParamType, str]] = ..., value: _Optional[int] = ...) -> None: ...
