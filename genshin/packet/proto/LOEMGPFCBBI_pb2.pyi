from genshin.packet.proto import PIAMLHKGKEE_pb2 as _PIAMLHKGKEE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOEMGPFCBBI(_message.Message):
    __slots__ = ("DAECIFFCAOP", "JGJMHGGKFFA", "NCCMFOLEPAC", "FHLCFPFAFIC", "KNNONDAGIMB")
    DAECIFFCAOP_FIELD_NUMBER: _ClassVar[int]
    JGJMHGGKFFA_FIELD_NUMBER: _ClassVar[int]
    NCCMFOLEPAC_FIELD_NUMBER: _ClassVar[int]
    FHLCFPFAFIC_FIELD_NUMBER: _ClassVar[int]
    KNNONDAGIMB_FIELD_NUMBER: _ClassVar[int]
    DAECIFFCAOP: _containers.RepeatedScalarFieldContainer[int]
    JGJMHGGKFFA: _containers.RepeatedScalarFieldContainer[int]
    NCCMFOLEPAC: _containers.RepeatedScalarFieldContainer[int]
    FHLCFPFAFIC: _containers.RepeatedCompositeFieldContainer[_PIAMLHKGKEE_pb2.PIAMLHKGKEE]
    KNNONDAGIMB: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, DAECIFFCAOP: _Optional[_Iterable[int]] = ..., JGJMHGGKFFA: _Optional[_Iterable[int]] = ..., NCCMFOLEPAC: _Optional[_Iterable[int]] = ..., FHLCFPFAFIC: _Optional[_Iterable[_Union[_PIAMLHKGKEE_pb2.PIAMLHKGKEE, _Mapping]]] = ..., KNNONDAGIMB: _Optional[_Iterable[int]] = ...) -> None: ...
