from genshin.packet.proto import GAIOBFEADPD_pb2 as _GAIOBFEADPD_pb2
from genshin.packet.proto import DCDCNNPIFFK_pb2 as _DCDCNNPIFFK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AHPOELHGGPM(_message.Message):
    __slots__ = ("EFCDELGMMKG", "MCPPEKNBHFK", "KLMDAPCLGAP", "FBFDAKLPEFB", "OAJOOBGHAGM")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    MCPPEKNBHFK_FIELD_NUMBER: _ClassVar[int]
    KLMDAPCLGAP_FIELD_NUMBER: _ClassVar[int]
    FBFDAKLPEFB_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_GAIOBFEADPD_pb2.GAIOBFEADPD]
    MCPPEKNBHFK: int
    KLMDAPCLGAP: int
    FBFDAKLPEFB: _DCDCNNPIFFK_pb2.DCDCNNPIFFK
    OAJOOBGHAGM: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_GAIOBFEADPD_pb2.GAIOBFEADPD, _Mapping]]] = ..., MCPPEKNBHFK: _Optional[int] = ..., KLMDAPCLGAP: _Optional[int] = ..., FBFDAKLPEFB: _Optional[_Union[_DCDCNNPIFFK_pb2.DCDCNNPIFFK, str]] = ..., OAJOOBGHAGM: _Optional[int] = ...) -> None: ...
