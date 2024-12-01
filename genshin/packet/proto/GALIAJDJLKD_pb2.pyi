from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GALIAJDJLKD(_message.Message):
    __slots__ = ("store_type", "EJNINFFFKJP", "guid")
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    store_type: _StoreType_pb2.StoreType
    EJNINFFFKJP: int
    guid: int
    def __init__(self, store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., EJNINFFFKJP: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
