from genshin.packet.proto import BBLGHLDONID_pb2 as _BBLGHLDONID_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MIFIKPOHMNG(_message.Message):
    __slots__ = ("NKKCADBJEDL", "MPNJAOCKMAH")
    NKKCADBJEDL_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    NKKCADBJEDL: _containers.RepeatedCompositeFieldContainer[_BBLGHLDONID_pb2.BBLGHLDONID]
    MPNJAOCKMAH: int
    def __init__(self, NKKCADBJEDL: _Optional[_Iterable[_Union[_BBLGHLDONID_pb2.BBLGHLDONID, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
