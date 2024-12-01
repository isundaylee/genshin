from genshin.packet.proto import MDKGKHMHLMH_pb2 as _MDKGKHMHLMH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KCJMDCFPOBF(_message.Message):
    __slots__ = ("MIFPLAAKKFP", "MPNJAOCKMAH", "IIEILNHPCJI", "BFBMAFJFHJA")
    MIFPLAAKKFP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    IIEILNHPCJI_FIELD_NUMBER: _ClassVar[int]
    BFBMAFJFHJA_FIELD_NUMBER: _ClassVar[int]
    MIFPLAAKKFP: _containers.RepeatedCompositeFieldContainer[_MDKGKHMHLMH_pb2.MDKGKHMHLMH]
    MPNJAOCKMAH: int
    IIEILNHPCJI: int
    BFBMAFJFHJA: int
    def __init__(self, MIFPLAAKKFP: _Optional[_Iterable[_Union[_MDKGKHMHLMH_pb2.MDKGKHMHLMH, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., IIEILNHPCJI: _Optional[int] = ..., BFBMAFJFHJA: _Optional[int] = ...) -> None: ...
