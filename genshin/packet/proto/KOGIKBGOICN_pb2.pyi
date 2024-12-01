from genshin.packet.proto import PMKMGHKNMMO_pb2 as _PMKMGHKNMMO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KOGIKBGOICN(_message.Message):
    __slots__ = ("OKPFCGNINOP", "NEBKJMLKNID")
    class OKPFCGNINOPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PMKMGHKNMMO_pb2.PMKMGHKNMMO
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PMKMGHKNMMO_pb2.PMKMGHKNMMO, _Mapping]] = ...) -> None: ...
    OKPFCGNINOP_FIELD_NUMBER: _ClassVar[int]
    NEBKJMLKNID_FIELD_NUMBER: _ClassVar[int]
    OKPFCGNINOP: _containers.MessageMap[int, _PMKMGHKNMMO_pb2.PMKMGHKNMMO]
    NEBKJMLKNID: int
    def __init__(self, OKPFCGNINOP: _Optional[_Mapping[int, _PMKMGHKNMMO_pb2.PMKMGHKNMMO]] = ..., NEBKJMLKNID: _Optional[int] = ...) -> None: ...
