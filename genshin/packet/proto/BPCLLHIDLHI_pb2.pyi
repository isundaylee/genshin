from genshin.packet.proto import PJJLOIPPLND_pb2 as _PJJLOIPPLND_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BPCLLHIDLHI(_message.Message):
    __slots__ = ("EFCDELGMMKG", "MPNJAOCKMAH", "BODIEJCLGMB")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_PJJLOIPPLND_pb2.PJJLOIPPLND]
    MPNJAOCKMAH: int
    BODIEJCLGMB: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_PJJLOIPPLND_pb2.PJJLOIPPLND, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., BODIEJCLGMB: _Optional[int] = ...) -> None: ...
