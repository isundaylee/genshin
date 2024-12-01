from genshin.packet.proto import BJGHDOCNFNB_pb2 as _BJGHDOCNFNB_pb2
from genshin.packet.proto import PKFABBKAPPA_pb2 as _PKFABBKAPPA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BNAGCIBNCGO(_message.Message):
    __slots__ = ("INOPFNJGMGG", "HPIFLHEFLNG", "KMLIGBJPNEJ", "PCCHFPHGCJB", "LCNPGPKFEIO", "BLFOIDKFGGF", "GMDCMOCIJAB", "NMFPPOMDCAC", "EPPPBOLKBAC")
    INOPFNJGMGG_FIELD_NUMBER: _ClassVar[int]
    HPIFLHEFLNG_FIELD_NUMBER: _ClassVar[int]
    KMLIGBJPNEJ_FIELD_NUMBER: _ClassVar[int]
    PCCHFPHGCJB_FIELD_NUMBER: _ClassVar[int]
    LCNPGPKFEIO_FIELD_NUMBER: _ClassVar[int]
    BLFOIDKFGGF_FIELD_NUMBER: _ClassVar[int]
    GMDCMOCIJAB_FIELD_NUMBER: _ClassVar[int]
    NMFPPOMDCAC_FIELD_NUMBER: _ClassVar[int]
    EPPPBOLKBAC_FIELD_NUMBER: _ClassVar[int]
    INOPFNJGMGG: _containers.RepeatedCompositeFieldContainer[_BJGHDOCNFNB_pb2.BJGHDOCNFNB]
    HPIFLHEFLNG: _containers.RepeatedCompositeFieldContainer[_PKFABBKAPPA_pb2.PKFABBKAPPA]
    KMLIGBJPNEJ: int
    PCCHFPHGCJB: int
    LCNPGPKFEIO: int
    BLFOIDKFGGF: int
    GMDCMOCIJAB: int
    NMFPPOMDCAC: bool
    EPPPBOLKBAC: int
    def __init__(self, INOPFNJGMGG: _Optional[_Iterable[_Union[_BJGHDOCNFNB_pb2.BJGHDOCNFNB, _Mapping]]] = ..., HPIFLHEFLNG: _Optional[_Iterable[_Union[_PKFABBKAPPA_pb2.PKFABBKAPPA, _Mapping]]] = ..., KMLIGBJPNEJ: _Optional[int] = ..., PCCHFPHGCJB: _Optional[int] = ..., LCNPGPKFEIO: _Optional[int] = ..., BLFOIDKFGGF: _Optional[int] = ..., GMDCMOCIJAB: _Optional[int] = ..., NMFPPOMDCAC: bool = ..., EPPPBOLKBAC: _Optional[int] = ...) -> None: ...
