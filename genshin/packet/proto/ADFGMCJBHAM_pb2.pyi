from genshin.packet.proto import MCJCANJLBLH_pb2 as _MCJCANJLBLH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ADFGMCJBHAM(_message.Message):
    __slots__ = ("FACPIFGCBBK", "MPNJAOCKMAH", "HCJFDJHILAM", "DGGHONFDBGJ")
    FACPIFGCBBK_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    DGGHONFDBGJ_FIELD_NUMBER: _ClassVar[int]
    FACPIFGCBBK: _containers.RepeatedCompositeFieldContainer[_MCJCANJLBLH_pb2.MCJCANJLBLH]
    MPNJAOCKMAH: int
    HCJFDJHILAM: bool
    DGGHONFDBGJ: bool
    def __init__(self, FACPIFGCBBK: _Optional[_Iterable[_Union[_MCJCANJLBLH_pb2.MCJCANJLBLH, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., HCJFDJHILAM: bool = ..., DGGHONFDBGJ: bool = ...) -> None: ...
