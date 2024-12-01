from genshin.packet.proto import FDAMHALDDLI_pb2 as _FDAMHALDDLI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MFBGDFCDJEP(_message.Message):
    __slots__ = ("FAGJDJIGLON", "HCJFDJHILAM", "PDJEEAMMKJD", "MPNJAOCKMAH")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    PDJEEAMMKJD_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_FDAMHALDDLI_pb2.FDAMHALDDLI]
    HCJFDJHILAM: bool
    PDJEEAMMKJD: bool
    MPNJAOCKMAH: int
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_FDAMHALDDLI_pb2.FDAMHALDDLI, _Mapping]]] = ..., HCJFDJHILAM: bool = ..., PDJEEAMMKJD: bool = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
