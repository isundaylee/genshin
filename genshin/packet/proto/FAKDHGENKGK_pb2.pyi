from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FAKDHGENKGK(_message.Message):
    __slots__ = ("JBPMEFJKLCN", "store_type")
    JBPMEFJKLCN_FIELD_NUMBER: _ClassVar[int]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    JBPMEFJKLCN: _containers.RepeatedScalarFieldContainer[int]
    store_type: _StoreType_pb2.StoreType
    def __init__(self, JBPMEFJKLCN: _Optional[_Iterable[int]] = ..., store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ...) -> None: ...
