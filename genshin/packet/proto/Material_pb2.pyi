from genshin.packet.proto import MaterialDeleteInfo_pb2 as _MaterialDeleteInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Material(_message.Message):
    __slots__ = ("count", "delete_info")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETE_INFO_FIELD_NUMBER: _ClassVar[int]
    count: int
    delete_info: _MaterialDeleteInfo_pb2.MaterialDeleteInfo
    def __init__(self, count: _Optional[int] = ..., delete_info: _Optional[_Union[_MaterialDeleteInfo_pb2.MaterialDeleteInfo, _Mapping]] = ...) -> None: ...
