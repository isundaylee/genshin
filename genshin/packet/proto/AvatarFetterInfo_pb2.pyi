from genshin.packet.proto import AANALBNNPPL_pb2 as _AANALBNNPPL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarFetterInfo(_message.Message):
    __slots__ = ("PLOKNPKGHPB", "IJBEEBFDOOP", "CCLLABBCIPD", "DPBNMFDMBNF", "FDCFKLMINJH", "DFLHPOBNIPG")
    PLOKNPKGHPB_FIELD_NUMBER: _ClassVar[int]
    IJBEEBFDOOP_FIELD_NUMBER: _ClassVar[int]
    CCLLABBCIPD_FIELD_NUMBER: _ClassVar[int]
    DPBNMFDMBNF_FIELD_NUMBER: _ClassVar[int]
    FDCFKLMINJH_FIELD_NUMBER: _ClassVar[int]
    DFLHPOBNIPG_FIELD_NUMBER: _ClassVar[int]
    PLOKNPKGHPB: _containers.RepeatedCompositeFieldContainer[_AANALBNNPPL_pb2.AANALBNNPPL]
    IJBEEBFDOOP: _containers.RepeatedScalarFieldContainer[int]
    CCLLABBCIPD: _containers.RepeatedScalarFieldContainer[int]
    DPBNMFDMBNF: _containers.RepeatedScalarFieldContainer[int]
    FDCFKLMINJH: int
    DFLHPOBNIPG: int
    def __init__(self, PLOKNPKGHPB: _Optional[_Iterable[_Union[_AANALBNNPPL_pb2.AANALBNNPPL, _Mapping]]] = ..., IJBEEBFDOOP: _Optional[_Iterable[int]] = ..., CCLLABBCIPD: _Optional[_Iterable[int]] = ..., DPBNMFDMBNF: _Optional[_Iterable[int]] = ..., FDCFKLMINJH: _Optional[int] = ..., DFLHPOBNIPG: _Optional[int] = ...) -> None: ...
