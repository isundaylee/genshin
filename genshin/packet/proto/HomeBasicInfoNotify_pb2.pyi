from genshin.packet.proto import HomeBasicInfo_pb2 as _HomeBasicInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBasicInfoNotify(_message.Message):
    __slots__ = ("basic_info",)
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    basic_info: _HomeBasicInfo_pb2.HomeBasicInfo
    def __init__(self, basic_info: _Optional[_Union[_HomeBasicInfo_pb2.HomeBasicInfo, _Mapping]] = ...) -> None: ...
