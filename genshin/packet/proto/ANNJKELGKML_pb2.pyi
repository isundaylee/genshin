from genshin.packet.proto import IKDANDKMINO_pb2 as _IKDANDKMINO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ANNJKELGKML(_message.Message):
    __slots__ = ("CDFLGIIDFEF", "EDOJGAFAKDA", "NEKECFNAHOM", "MPNJAOCKMAH")
    CDFLGIIDFEF_FIELD_NUMBER: _ClassVar[int]
    EDOJGAFAKDA_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    CDFLGIIDFEF: _containers.RepeatedCompositeFieldContainer[_IKDANDKMINO_pb2.IKDANDKMINO]
    EDOJGAFAKDA: bool
    NEKECFNAHOM: int
    MPNJAOCKMAH: int
    def __init__(self, CDFLGIIDFEF: _Optional[_Iterable[_Union[_IKDANDKMINO_pb2.IKDANDKMINO, _Mapping]]] = ..., EDOJGAFAKDA: bool = ..., NEKECFNAHOM: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
