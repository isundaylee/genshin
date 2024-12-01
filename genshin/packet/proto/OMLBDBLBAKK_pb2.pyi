from genshin.packet.proto import MKNEAMDHFFN_pb2 as _MKNEAMDHFFN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OMLBDBLBAKK(_message.Message):
    __slots__ = ("OCAFMMJENEC", "FEPDFDJHLHP", "IBOFHCJMFNI", "EHKDKEMONBL", "BMFAADBOCFN")
    OCAFMMJENEC_FIELD_NUMBER: _ClassVar[int]
    FEPDFDJHLHP_FIELD_NUMBER: _ClassVar[int]
    IBOFHCJMFNI_FIELD_NUMBER: _ClassVar[int]
    EHKDKEMONBL_FIELD_NUMBER: _ClassVar[int]
    BMFAADBOCFN_FIELD_NUMBER: _ClassVar[int]
    OCAFMMJENEC: _containers.RepeatedScalarFieldContainer[int]
    FEPDFDJHLHP: _containers.RepeatedScalarFieldContainer[int]
    IBOFHCJMFNI: _containers.RepeatedCompositeFieldContainer[_MKNEAMDHFFN_pb2.MKNEAMDHFFN]
    EHKDKEMONBL: _containers.RepeatedCompositeFieldContainer[_MKNEAMDHFFN_pb2.MKNEAMDHFFN]
    BMFAADBOCFN: bool
    def __init__(self, OCAFMMJENEC: _Optional[_Iterable[int]] = ..., FEPDFDJHLHP: _Optional[_Iterable[int]] = ..., IBOFHCJMFNI: _Optional[_Iterable[_Union[_MKNEAMDHFFN_pb2.MKNEAMDHFFN, _Mapping]]] = ..., EHKDKEMONBL: _Optional[_Iterable[_Union[_MKNEAMDHFFN_pb2.MKNEAMDHFFN, _Mapping]]] = ..., BMFAADBOCFN: bool = ...) -> None: ...
