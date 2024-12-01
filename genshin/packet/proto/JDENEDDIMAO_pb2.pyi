from genshin.packet.proto import NBJPCHJJCNJ_pb2 as _NBJPCHJJCNJ_pb2
from genshin.packet.proto import PIMMBIDLDCL_pb2 as _PIMMBIDLDCL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JDENEDDIMAO(_message.Message):
    __slots__ = ("ONCFEKCFKMO", "KKPPJFKDDEP", "MPNJAOCKMAH")
    ONCFEKCFKMO_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    ONCFEKCFKMO: _containers.RepeatedCompositeFieldContainer[_NBJPCHJJCNJ_pb2.NBJPCHJJCNJ]
    KKPPJFKDDEP: _PIMMBIDLDCL_pb2.PIMMBIDLDCL
    MPNJAOCKMAH: int
    def __init__(self, ONCFEKCFKMO: _Optional[_Iterable[_Union[_NBJPCHJJCNJ_pb2.NBJPCHJJCNJ, _Mapping]]] = ..., KKPPJFKDDEP: _Optional[_Union[_PIMMBIDLDCL_pb2.PIMMBIDLDCL, str]] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
