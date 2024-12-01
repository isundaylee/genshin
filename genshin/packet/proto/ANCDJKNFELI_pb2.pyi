from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ANCDJKNFELI(_message.Message):
    __slots__ = ("HCEJPKIAJAP", "ODCMKOFFKKL", "MPNJAOCKMAH", "EDNALCKIJPG", "FEDJBGPLMHI", "MONEJDBPOLB", "DPBDBMIIOMP", "JCHHJFLDLGA", "OMENIAMEDCE")
    HCEJPKIAJAP_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    EDNALCKIJPG_FIELD_NUMBER: _ClassVar[int]
    FEDJBGPLMHI_FIELD_NUMBER: _ClassVar[int]
    MONEJDBPOLB_FIELD_NUMBER: _ClassVar[int]
    DPBDBMIIOMP_FIELD_NUMBER: _ClassVar[int]
    JCHHJFLDLGA_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    HCEJPKIAJAP: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    ODCMKOFFKKL: int
    MPNJAOCKMAH: int
    EDNALCKIJPG: int
    FEDJBGPLMHI: int
    MONEJDBPOLB: int
    DPBDBMIIOMP: int
    JCHHJFLDLGA: bool
    OMENIAMEDCE: bool
    def __init__(self, HCEJPKIAJAP: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., ODCMKOFFKKL: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., EDNALCKIJPG: _Optional[int] = ..., FEDJBGPLMHI: _Optional[int] = ..., MONEJDBPOLB: _Optional[int] = ..., DPBDBMIIOMP: _Optional[int] = ..., JCHHJFLDLGA: bool = ..., OMENIAMEDCE: bool = ...) -> None: ...
