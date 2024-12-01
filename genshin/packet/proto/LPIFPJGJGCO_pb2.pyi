from genshin.packet.proto import LDCECHMBPFH_pb2 as _LDCECHMBPFH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LPIFPJGJGCO(_message.Message):
    __slots__ = ("CAEPGNAFCCK", "guid")
    CAEPGNAFCCK_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    CAEPGNAFCCK: _LDCECHMBPFH_pb2.LDCECHMBPFH
    guid: int
    def __init__(self, CAEPGNAFCCK: _Optional[_Union[_LDCECHMBPFH_pb2.LDCECHMBPFH, _Mapping]] = ..., guid: _Optional[int] = ...) -> None: ...
