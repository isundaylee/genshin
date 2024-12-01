from genshin.packet.proto import NMKNDNHOPPM_pb2 as _NMKNDNHOPPM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MDDAGBICMKE(_message.Message):
    __slots__ = ("HAJOLEIPGNP", "HGGEHLMHKMP", "IBCPGOOAJKG")
    class HAJOLEIPGNPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NMKNDNHOPPM_pb2.NMKNDNHOPPM
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NMKNDNHOPPM_pb2.NMKNDNHOPPM, _Mapping]] = ...) -> None: ...
    HAJOLEIPGNP_FIELD_NUMBER: _ClassVar[int]
    HGGEHLMHKMP_FIELD_NUMBER: _ClassVar[int]
    IBCPGOOAJKG_FIELD_NUMBER: _ClassVar[int]
    HAJOLEIPGNP: _containers.MessageMap[int, _NMKNDNHOPPM_pb2.NMKNDNHOPPM]
    HGGEHLMHKMP: int
    IBCPGOOAJKG: int
    def __init__(self, HAJOLEIPGNP: _Optional[_Mapping[int, _NMKNDNHOPPM_pb2.NMKNDNHOPPM]] = ..., HGGEHLMHKMP: _Optional[int] = ..., IBCPGOOAJKG: _Optional[int] = ...) -> None: ...
