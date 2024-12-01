from genshin.packet.proto import PMNBPEPIJIK_pb2 as _PMNBPEPIJIK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MAHBLNHANCC(_message.Message):
    __slots__ = ("OIIPLHCBIOK", "CPHMIDONIPH", "BKPHJKHILOD")
    OIIPLHCBIOK_FIELD_NUMBER: _ClassVar[int]
    CPHMIDONIPH_FIELD_NUMBER: _ClassVar[int]
    BKPHJKHILOD_FIELD_NUMBER: _ClassVar[int]
    OIIPLHCBIOK: _containers.RepeatedCompositeFieldContainer[_PMNBPEPIJIK_pb2.PMNBPEPIJIK]
    CPHMIDONIPH: int
    BKPHJKHILOD: int
    def __init__(self, OIIPLHCBIOK: _Optional[_Iterable[_Union[_PMNBPEPIJIK_pb2.PMNBPEPIJIK, _Mapping]]] = ..., CPHMIDONIPH: _Optional[int] = ..., BKPHJKHILOD: _Optional[int] = ...) -> None: ...
