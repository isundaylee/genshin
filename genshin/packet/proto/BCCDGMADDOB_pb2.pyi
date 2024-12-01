from genshin.packet.proto import LJCIAEFKOOA_pb2 as _LJCIAEFKOOA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BCCDGMADDOB(_message.Message):
    __slots__ = ("BOLPFLHNIPI", "GMDCMOCIJAB", "POAOHGGJFEL", "OALIOHAMLGN", "APFDCPLLHEB", "MPFLDFDOGAI", "NMIKCMLKNDM")
    BOLPFLHNIPI_FIELD_NUMBER: _ClassVar[int]
    GMDCMOCIJAB_FIELD_NUMBER: _ClassVar[int]
    POAOHGGJFEL_FIELD_NUMBER: _ClassVar[int]
    OALIOHAMLGN_FIELD_NUMBER: _ClassVar[int]
    APFDCPLLHEB_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    BOLPFLHNIPI: _containers.RepeatedCompositeFieldContainer[_LJCIAEFKOOA_pb2.LJCIAEFKOOA]
    GMDCMOCIJAB: int
    POAOHGGJFEL: int
    OALIOHAMLGN: int
    APFDCPLLHEB: bool
    MPFLDFDOGAI: bool
    NMIKCMLKNDM: int
    def __init__(self, BOLPFLHNIPI: _Optional[_Iterable[_Union[_LJCIAEFKOOA_pb2.LJCIAEFKOOA, _Mapping]]] = ..., GMDCMOCIJAB: _Optional[int] = ..., POAOHGGJFEL: _Optional[int] = ..., OALIOHAMLGN: _Optional[int] = ..., APFDCPLLHEB: bool = ..., MPFLDFDOGAI: bool = ..., NMIKCMLKNDM: _Optional[int] = ...) -> None: ...
