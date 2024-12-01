from genshin.packet.proto import OCAABICBPNI_pb2 as _OCAABICBPNI_pb2
from genshin.packet.proto import FPAHDFLMHND_pb2 as _FPAHDFLMHND_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFBMJKMEFLM(_message.Message):
    __slots__ = ("COPAAFJHPGD", "KABODNMEGEK", "MPNJAOCKMAH", "NEKECFNAHOM")
    COPAAFJHPGD_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    COPAAFJHPGD: _containers.RepeatedCompositeFieldContainer[_OCAABICBPNI_pb2.OCAABICBPNI]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_FPAHDFLMHND_pb2.FPAHDFLMHND]
    MPNJAOCKMAH: int
    NEKECFNAHOM: int
    def __init__(self, COPAAFJHPGD: _Optional[_Iterable[_Union[_OCAABICBPNI_pb2.OCAABICBPNI, _Mapping]]] = ..., KABODNMEGEK: _Optional[_Iterable[_Union[_FPAHDFLMHND_pb2.FPAHDFLMHND, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., NEKECFNAHOM: _Optional[int] = ...) -> None: ...
