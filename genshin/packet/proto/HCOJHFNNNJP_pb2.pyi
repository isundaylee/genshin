from genshin.packet.proto import GFFIOKDNCLP_pb2 as _GFFIOKDNCLP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HCOJHFNNNJP(_message.Message):
    __slots__ = ("FHCFDLFLKNO", "BJHOPIEGDGE", "HHAIIFODEOO", "BOFFIDCGJEM", "EGJDKPKGDIB", "IGBDOEBPPHO", "ILAHFKPDAGK")
    FHCFDLFLKNO_FIELD_NUMBER: _ClassVar[int]
    BJHOPIEGDGE_FIELD_NUMBER: _ClassVar[int]
    HHAIIFODEOO_FIELD_NUMBER: _ClassVar[int]
    BOFFIDCGJEM_FIELD_NUMBER: _ClassVar[int]
    EGJDKPKGDIB_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    ILAHFKPDAGK_FIELD_NUMBER: _ClassVar[int]
    FHCFDLFLKNO: _containers.RepeatedCompositeFieldContainer[_GFFIOKDNCLP_pb2.GFFIOKDNCLP]
    BJHOPIEGDGE: _containers.RepeatedScalarFieldContainer[int]
    HHAIIFODEOO: int
    BOFFIDCGJEM: int
    EGJDKPKGDIB: int
    IGBDOEBPPHO: int
    ILAHFKPDAGK: bool
    def __init__(self, FHCFDLFLKNO: _Optional[_Iterable[_Union[_GFFIOKDNCLP_pb2.GFFIOKDNCLP, _Mapping]]] = ..., BJHOPIEGDGE: _Optional[_Iterable[int]] = ..., HHAIIFODEOO: _Optional[int] = ..., BOFFIDCGJEM: _Optional[int] = ..., EGJDKPKGDIB: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ..., ILAHFKPDAGK: bool = ...) -> None: ...
