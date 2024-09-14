from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreItemDelNotify(_message.Message):
    __slots__ = ("store_type", "guid_list")
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    store_type: _StoreType_pb2.StoreType
    guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
