from genshin.packet.proto import DJFNBCGCGCP_pb2 as _DJFNBCGCGCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ACFCEBAEFNP(_message.Message):
    __slots__ = ("MHMPLDDOKKO", "AKGEOCOBNBF", "MPNJAOCKMAH", "BODIEJCLGMB", "JFFPLOJAEMP")
    MHMPLDDOKKO_FIELD_NUMBER: _ClassVar[int]
    AKGEOCOBNBF_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    JFFPLOJAEMP_FIELD_NUMBER: _ClassVar[int]
    MHMPLDDOKKO: _containers.RepeatedCompositeFieldContainer[_DJFNBCGCGCP_pb2.DJFNBCGCGCP]
    AKGEOCOBNBF: _containers.RepeatedCompositeFieldContainer[_DJFNBCGCGCP_pb2.DJFNBCGCGCP]
    MPNJAOCKMAH: int
    BODIEJCLGMB: int
    JFFPLOJAEMP: bool
    def __init__(self, MHMPLDDOKKO: _Optional[_Iterable[_Union[_DJFNBCGCGCP_pb2.DJFNBCGCGCP, _Mapping]]] = ..., AKGEOCOBNBF: _Optional[_Iterable[_Union[_DJFNBCGCGCP_pb2.DJFNBCGCGCP, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., BODIEJCLGMB: _Optional[int] = ..., JFFPLOJAEMP: bool = ...) -> None: ...
