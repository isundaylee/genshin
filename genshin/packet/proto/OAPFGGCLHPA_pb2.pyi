from genshin.packet.proto import MPNDGCPKCFN_pb2 as _MPNDGCPKCFN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAPFGGCLHPA(_message.Message):
    __slots__ = ("EILAHBHKMED", "HCJFDJHILAM", "GOONOOPFOAM", "LBEINAHAHKA", "NILALKPFCCO", "OELCNLOJHHE")
    EILAHBHKMED_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    GOONOOPFOAM_FIELD_NUMBER: _ClassVar[int]
    LBEINAHAHKA_FIELD_NUMBER: _ClassVar[int]
    NILALKPFCCO_FIELD_NUMBER: _ClassVar[int]
    OELCNLOJHHE_FIELD_NUMBER: _ClassVar[int]
    EILAHBHKMED: _containers.RepeatedCompositeFieldContainer[_MPNDGCPKCFN_pb2.MPNDGCPKCFN]
    HCJFDJHILAM: bool
    GOONOOPFOAM: bool
    LBEINAHAHKA: int
    NILALKPFCCO: int
    OELCNLOJHHE: int
    def __init__(self, EILAHBHKMED: _Optional[_Iterable[_Union[_MPNDGCPKCFN_pb2.MPNDGCPKCFN, _Mapping]]] = ..., HCJFDJHILAM: bool = ..., GOONOOPFOAM: bool = ..., LBEINAHAHKA: _Optional[int] = ..., NILALKPFCCO: _Optional[int] = ..., OELCNLOJHHE: _Optional[int] = ...) -> None: ...
