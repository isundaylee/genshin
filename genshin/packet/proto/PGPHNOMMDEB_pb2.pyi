from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PGPHNOMMDEB(_message.Message):
    __slots__ = ("ILCFMFPNMNA", "MNCHCGGMLPA", "NCCPPHNNPBF")
    ILCFMFPNMNA_FIELD_NUMBER: _ClassVar[int]
    MNCHCGGMLPA_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    ILCFMFPNMNA: _containers.RepeatedScalarFieldContainer[int]
    MNCHCGGMLPA: _containers.RepeatedScalarFieldContainer[int]
    NCCPPHNNPBF: int
    def __init__(self, ILCFMFPNMNA: _Optional[_Iterable[int]] = ..., MNCHCGGMLPA: _Optional[_Iterable[int]] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...