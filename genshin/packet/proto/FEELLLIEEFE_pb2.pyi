from genshin.packet.proto import OFBHCGGGGGN_pb2 as _OFBHCGGGGGN_pb2
from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from genshin.packet.proto import IMGPEMFGOPF_pb2 as _IMGPEMFGOPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FEELLLIEEFE(_message.Message):
    __slots__ = ("FMIEBPKJJPJ", "CAINBBIBGEB", "OAJOOBGHAGM", "COKCGKDPPEM", "FDLPBGMPMNL", "MIBHHJEDEPE", "HIACPELKDMP", "AMOHEAPPLCA")
    class FMIEBPKJJPJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _OFBHCGGGGGN_pb2.OFBHCGGGGGN
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_OFBHCGGGGGN_pb2.OFBHCGGGGGN, _Mapping]] = ...) -> None: ...
    FMIEBPKJJPJ_FIELD_NUMBER: _ClassVar[int]
    CAINBBIBGEB_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    COKCGKDPPEM_FIELD_NUMBER: _ClassVar[int]
    FDLPBGMPMNL_FIELD_NUMBER: _ClassVar[int]
    MIBHHJEDEPE_FIELD_NUMBER: _ClassVar[int]
    HIACPELKDMP_FIELD_NUMBER: _ClassVar[int]
    AMOHEAPPLCA_FIELD_NUMBER: _ClassVar[int]
    FMIEBPKJJPJ: _containers.MessageMap[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]
    CAINBBIBGEB: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    OAJOOBGHAGM: int
    COKCGKDPPEM: _IMGPEMFGOPF_pb2.IMGPEMFGOPF
    FDLPBGMPMNL: int
    MIBHHJEDEPE: int
    HIACPELKDMP: int
    AMOHEAPPLCA: int
    def __init__(self, FMIEBPKJJPJ: _Optional[_Mapping[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]] = ..., CAINBBIBGEB: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., OAJOOBGHAGM: _Optional[int] = ..., COKCGKDPPEM: _Optional[_Union[_IMGPEMFGOPF_pb2.IMGPEMFGOPF, str]] = ..., FDLPBGMPMNL: _Optional[int] = ..., MIBHHJEDEPE: _Optional[int] = ..., HIACPELKDMP: _Optional[int] = ..., AMOHEAPPLCA: _Optional[int] = ...) -> None: ...
