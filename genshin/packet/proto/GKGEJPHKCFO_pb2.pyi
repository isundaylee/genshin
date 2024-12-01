from genshin.packet.proto import PHADDBEDDGK_pb2 as _PHADDBEDDGK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GKGEJPHKCFO(_message.Message):
    __slots__ = ("EFCDELGMMKG", "MJAONINHIIB", "AELJDIPLELM", "EAIPGEMKNPO", "MPNJAOCKMAH")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    MJAONINHIIB_FIELD_NUMBER: _ClassVar[int]
    AELJDIPLELM_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_PHADDBEDDGK_pb2.PHADDBEDDGK]
    MJAONINHIIB: _containers.RepeatedScalarFieldContainer[int]
    AELJDIPLELM: int
    EAIPGEMKNPO: int
    MPNJAOCKMAH: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_PHADDBEDDGK_pb2.PHADDBEDDGK, _Mapping]]] = ..., MJAONINHIIB: _Optional[_Iterable[int]] = ..., AELJDIPLELM: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
