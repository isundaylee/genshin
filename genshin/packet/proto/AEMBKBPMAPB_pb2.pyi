from genshin.packet.proto import DJCGMLCFKLC_pb2 as _DJCGMLCFKLC_pb2
from genshin.packet.proto import DGBLPHDFCBI_pb2 as _DGBLPHDFCBI_pb2
from genshin.packet.proto import JKLPNOGHIOI_pb2 as _JKLPNOGHIOI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEMBKBPMAPB(_message.Message):
    __slots__ = ("DCLKHFDNIFN", "DMBCGDCNJJP", "KCKEPCMLIHI", "CKICLLDGHGH", "KFPHMNGHBFG")
    DCLKHFDNIFN_FIELD_NUMBER: _ClassVar[int]
    DMBCGDCNJJP_FIELD_NUMBER: _ClassVar[int]
    KCKEPCMLIHI_FIELD_NUMBER: _ClassVar[int]
    CKICLLDGHGH_FIELD_NUMBER: _ClassVar[int]
    KFPHMNGHBFG_FIELD_NUMBER: _ClassVar[int]
    DCLKHFDNIFN: _containers.RepeatedCompositeFieldContainer[_DJCGMLCFKLC_pb2.DJCGMLCFKLC]
    DMBCGDCNJJP: _containers.RepeatedScalarFieldContainer[int]
    KCKEPCMLIHI: _containers.RepeatedCompositeFieldContainer[_DGBLPHDFCBI_pb2.DGBLPHDFCBI]
    CKICLLDGHGH: _containers.RepeatedCompositeFieldContainer[_JKLPNOGHIOI_pb2.JKLPNOGHIOI]
    KFPHMNGHBFG: int
    def __init__(self, DCLKHFDNIFN: _Optional[_Iterable[_Union[_DJCGMLCFKLC_pb2.DJCGMLCFKLC, _Mapping]]] = ..., DMBCGDCNJJP: _Optional[_Iterable[int]] = ..., KCKEPCMLIHI: _Optional[_Iterable[_Union[_DGBLPHDFCBI_pb2.DGBLPHDFCBI, _Mapping]]] = ..., CKICLLDGHGH: _Optional[_Iterable[_Union[_JKLPNOGHIOI_pb2.JKLPNOGHIOI, _Mapping]]] = ..., KFPHMNGHBFG: _Optional[int] = ...) -> None: ...
