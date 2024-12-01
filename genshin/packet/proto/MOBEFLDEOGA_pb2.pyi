from genshin.packet.proto import GJDJPCPPHIC_pb2 as _GJDJPCPPHIC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MOBEFLDEOGA(_message.Message):
    __slots__ = ("APOCDMCGEBC", "EPNDBDPKLEP", "MNDHNPJNNGP")
    APOCDMCGEBC_FIELD_NUMBER: _ClassVar[int]
    EPNDBDPKLEP_FIELD_NUMBER: _ClassVar[int]
    MNDHNPJNNGP_FIELD_NUMBER: _ClassVar[int]
    APOCDMCGEBC: _containers.RepeatedScalarFieldContainer[int]
    EPNDBDPKLEP: _GJDJPCPPHIC_pb2.GJDJPCPPHIC
    MNDHNPJNNGP: int
    def __init__(self, APOCDMCGEBC: _Optional[_Iterable[int]] = ..., EPNDBDPKLEP: _Optional[_Union[_GJDJPCPPHIC_pb2.GJDJPCPPHIC, _Mapping]] = ..., MNDHNPJNNGP: _Optional[int] = ...) -> None: ...
