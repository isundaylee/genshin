from genshin.packet.proto import PBCDOHBBLNH_pb2 as _PBCDOHBBLNH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JGCFLHEDIHI(_message.Message):
    __slots__ = ("DHILGECCJDK", "GJAIFGLOAAJ", "MNIFAHPFIKO", "KMGLDKLANFJ", "FMBBPNHCCIA", "ABNHMHDLOKH")
    DHILGECCJDK_FIELD_NUMBER: _ClassVar[int]
    GJAIFGLOAAJ_FIELD_NUMBER: _ClassVar[int]
    MNIFAHPFIKO_FIELD_NUMBER: _ClassVar[int]
    KMGLDKLANFJ_FIELD_NUMBER: _ClassVar[int]
    FMBBPNHCCIA_FIELD_NUMBER: _ClassVar[int]
    ABNHMHDLOKH_FIELD_NUMBER: _ClassVar[int]
    DHILGECCJDK: _containers.RepeatedCompositeFieldContainer[_PBCDOHBBLNH_pb2.PBCDOHBBLNH]
    GJAIFGLOAAJ: bool
    MNIFAHPFIKO: bool
    KMGLDKLANFJ: int
    FMBBPNHCCIA: int
    ABNHMHDLOKH: float
    def __init__(self, DHILGECCJDK: _Optional[_Iterable[_Union[_PBCDOHBBLNH_pb2.PBCDOHBBLNH, _Mapping]]] = ..., GJAIFGLOAAJ: bool = ..., MNIFAHPFIKO: bool = ..., KMGLDKLANFJ: _Optional[int] = ..., FMBBPNHCCIA: _Optional[int] = ..., ABNHMHDLOKH: _Optional[float] = ...) -> None: ...
