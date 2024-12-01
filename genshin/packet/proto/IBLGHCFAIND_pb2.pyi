from genshin.packet.proto import PKGOCLIMOIG_pb2 as _PKGOCLIMOIG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IBLGHCFAIND(_message.Message):
    __slots__ = ("MAOIJFFGIDE", "BPDLJHGNNGD", "MPNJAOCKMAH")
    MAOIJFFGIDE_FIELD_NUMBER: _ClassVar[int]
    BPDLJHGNNGD_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    MAOIJFFGIDE: _containers.RepeatedCompositeFieldContainer[_PKGOCLIMOIG_pb2.PKGOCLIMOIG]
    BPDLJHGNNGD: bool
    MPNJAOCKMAH: int
    def __init__(self, MAOIJFFGIDE: _Optional[_Iterable[_Union[_PKGOCLIMOIG_pb2.PKGOCLIMOIG, _Mapping]]] = ..., BPDLJHGNNGD: bool = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
