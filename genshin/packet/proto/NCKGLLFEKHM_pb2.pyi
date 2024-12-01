from genshin.packet.proto import MGOAEAIGBOK_pb2 as _MGOAEAIGBOK_pb2
from genshin.packet.proto import CMBDNHPIFCH_pb2 as _CMBDNHPIFCH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NCKGLLFEKHM(_message.Message):
    __slots__ = ("LHEBDOBKEMJ", "NGLGKLAEAFK", "OGEDLBMHNIM", "FEOGJLNKGHA")
    LHEBDOBKEMJ_FIELD_NUMBER: _ClassVar[int]
    NGLGKLAEAFK_FIELD_NUMBER: _ClassVar[int]
    OGEDLBMHNIM_FIELD_NUMBER: _ClassVar[int]
    FEOGJLNKGHA_FIELD_NUMBER: _ClassVar[int]
    LHEBDOBKEMJ: _containers.RepeatedScalarFieldContainer[int]
    NGLGKLAEAFK: _containers.RepeatedCompositeFieldContainer[_MGOAEAIGBOK_pb2.MGOAEAIGBOK]
    OGEDLBMHNIM: _containers.RepeatedScalarFieldContainer[int]
    FEOGJLNKGHA: _containers.RepeatedCompositeFieldContainer[_CMBDNHPIFCH_pb2.CMBDNHPIFCH]
    def __init__(self, LHEBDOBKEMJ: _Optional[_Iterable[int]] = ..., NGLGKLAEAFK: _Optional[_Iterable[_Union[_MGOAEAIGBOK_pb2.MGOAEAIGBOK, _Mapping]]] = ..., OGEDLBMHNIM: _Optional[_Iterable[int]] = ..., FEOGJLNKGHA: _Optional[_Iterable[_Union[_CMBDNHPIFCH_pb2.CMBDNHPIFCH, _Mapping]]] = ...) -> None: ...
