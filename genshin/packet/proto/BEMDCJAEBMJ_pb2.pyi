from genshin.packet.proto import CGGELDLHDAJ_pb2 as _CGGELDLHDAJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BEMDCJAEBMJ(_message.Message):
    __slots__ = ("ADMIAGBHJMO", "AJCPNHFKAOO")
    ADMIAGBHJMO_FIELD_NUMBER: _ClassVar[int]
    AJCPNHFKAOO_FIELD_NUMBER: _ClassVar[int]
    ADMIAGBHJMO: _containers.RepeatedScalarFieldContainer[int]
    AJCPNHFKAOO: _containers.RepeatedCompositeFieldContainer[_CGGELDLHDAJ_pb2.CGGELDLHDAJ]
    def __init__(self, ADMIAGBHJMO: _Optional[_Iterable[int]] = ..., AJCPNHFKAOO: _Optional[_Iterable[_Union[_CGGELDLHDAJ_pb2.CGGELDLHDAJ, _Mapping]]] = ...) -> None: ...
