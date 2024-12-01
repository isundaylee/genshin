from genshin.packet.proto import FBLPIKDDJDN_pb2 as _FBLPIKDDJDN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KMKIAAKGNPH(_message.Message):
    __slots__ = ("EFCDELGMMKG", "MPNJAOCKMAH", "DMMELIMGOAJ", "OPPHIOANEBB", "EAIPGEMKNPO")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    DMMELIMGOAJ_FIELD_NUMBER: _ClassVar[int]
    OPPHIOANEBB_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_FBLPIKDDJDN_pb2.FBLPIKDDJDN]
    MPNJAOCKMAH: int
    DMMELIMGOAJ: int
    OPPHIOANEBB: int
    EAIPGEMKNPO: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_FBLPIKDDJDN_pb2.FBLPIKDDJDN, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., DMMELIMGOAJ: _Optional[int] = ..., OPPHIOANEBB: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
