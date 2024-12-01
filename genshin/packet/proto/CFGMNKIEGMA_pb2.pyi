from genshin.packet.proto import AvatarFetterInfo_pb2 as _AvatarFetterInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CFGMNKIEGMA(_message.Message):
    __slots__ = ("LJJFHEAJDHA",)
    class LJJFHEAJDHAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarFetterInfo_pb2.AvatarFetterInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarFetterInfo_pb2.AvatarFetterInfo, _Mapping]] = ...) -> None: ...
    LJJFHEAJDHA_FIELD_NUMBER: _ClassVar[int]
    LJJFHEAJDHA: _containers.MessageMap[int, _AvatarFetterInfo_pb2.AvatarFetterInfo]
    def __init__(self, LJJFHEAJDHA: _Optional[_Mapping[int, _AvatarFetterInfo_pb2.AvatarFetterInfo]] = ...) -> None: ...
