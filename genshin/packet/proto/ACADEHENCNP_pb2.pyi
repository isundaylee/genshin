from genshin.packet.proto import HIAOJLHGGDK_pb2 as _HIAOJLHGGDK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ACADEHENCNP(_message.Message):
    __slots__ = ("BELOKFABIJF", "EJNINFFFKJP")
    class BELOKFABIJFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HIAOJLHGGDK_pb2.HIAOJLHGGDK
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HIAOJLHGGDK_pb2.HIAOJLHGGDK, _Mapping]] = ...) -> None: ...
    BELOKFABIJF_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BELOKFABIJF: _containers.MessageMap[int, _HIAOJLHGGDK_pb2.HIAOJLHGGDK]
    EJNINFFFKJP: int
    def __init__(self, BELOKFABIJF: _Optional[_Mapping[int, _HIAOJLHGGDK_pb2.HIAOJLHGGDK]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
