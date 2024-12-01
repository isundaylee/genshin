from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from genshin.packet.proto import IMGPEMFGOPF_pb2 as _IMGPEMFGOPF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IBEKDFANAPI(_message.Message):
    __slots__ = ("CAINBBIBGEB", "AMOHEAPPLCA", "COKCGKDPPEM", "HIACPELKDMP")
    CAINBBIBGEB_FIELD_NUMBER: _ClassVar[int]
    AMOHEAPPLCA_FIELD_NUMBER: _ClassVar[int]
    COKCGKDPPEM_FIELD_NUMBER: _ClassVar[int]
    HIACPELKDMP_FIELD_NUMBER: _ClassVar[int]
    CAINBBIBGEB: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    AMOHEAPPLCA: int
    COKCGKDPPEM: _IMGPEMFGOPF_pb2.IMGPEMFGOPF
    HIACPELKDMP: int
    def __init__(self, CAINBBIBGEB: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., AMOHEAPPLCA: _Optional[int] = ..., COKCGKDPPEM: _Optional[_Union[_IMGPEMFGOPF_pb2.IMGPEMFGOPF, str]] = ..., HIACPELKDMP: _Optional[int] = ...) -> None: ...
