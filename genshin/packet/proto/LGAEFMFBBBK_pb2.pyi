from genshin.packet.proto import OHFHHIEJGIP_pb2 as _OHFHHIEJGIP_pb2
from genshin.packet.proto import MKDEKEFNKLF_pb2 as _MKDEKEFNKLF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LGAEFMFBBBK(_message.Message):
    __slots__ = ("CMLDOOJCJHK", "DMBMJAIIGEC", "HECNCAMMJDO", "FPDNLPHAJOJ", "ADHIBDAJPNK", "FIDDPFBIMIF")
    CMLDOOJCJHK_FIELD_NUMBER: _ClassVar[int]
    DMBMJAIIGEC_FIELD_NUMBER: _ClassVar[int]
    HECNCAMMJDO_FIELD_NUMBER: _ClassVar[int]
    FPDNLPHAJOJ_FIELD_NUMBER: _ClassVar[int]
    ADHIBDAJPNK_FIELD_NUMBER: _ClassVar[int]
    FIDDPFBIMIF_FIELD_NUMBER: _ClassVar[int]
    CMLDOOJCJHK: _OHFHHIEJGIP_pb2.OHFHHIEJGIP
    DMBMJAIIGEC: _containers.RepeatedCompositeFieldContainer[_MKDEKEFNKLF_pb2.MKDEKEFNKLF]
    HECNCAMMJDO: bool
    FPDNLPHAJOJ: bool
    ADHIBDAJPNK: bool
    FIDDPFBIMIF: int
    def __init__(self, CMLDOOJCJHK: _Optional[_Union[_OHFHHIEJGIP_pb2.OHFHHIEJGIP, _Mapping]] = ..., DMBMJAIIGEC: _Optional[_Iterable[_Union[_MKDEKEFNKLF_pb2.MKDEKEFNKLF, _Mapping]]] = ..., HECNCAMMJDO: bool = ..., FPDNLPHAJOJ: bool = ..., ADHIBDAJPNK: bool = ..., FIDDPFBIMIF: _Optional[int] = ...) -> None: ...
