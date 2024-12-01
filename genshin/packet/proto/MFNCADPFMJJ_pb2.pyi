from genshin.packet.proto import LHDNOHDMIMO_pb2 as _LHDNOHDMIMO_pb2
from genshin.packet.proto import DOKKNIDHJOB_pb2 as _DOKKNIDHJOB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MFNCADPFMJJ(_message.Message):
    __slots__ = ("NEHPGMLDKMF", "LKKKDNOHCIG", "AMLIJKENIIN", "ONKGKHGAFHJ", "NJPJCGCNEDO", "MPNJAOCKMAH", "MONEJDBPOLB", "NCPPELGEFPN", "HCJFDJHILAM")
    NEHPGMLDKMF_FIELD_NUMBER: _ClassVar[int]
    LKKKDNOHCIG_FIELD_NUMBER: _ClassVar[int]
    AMLIJKENIIN_FIELD_NUMBER: _ClassVar[int]
    ONKGKHGAFHJ_FIELD_NUMBER: _ClassVar[int]
    NJPJCGCNEDO_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    MONEJDBPOLB_FIELD_NUMBER: _ClassVar[int]
    NCPPELGEFPN_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    NEHPGMLDKMF: _containers.RepeatedCompositeFieldContainer[_LHDNOHDMIMO_pb2.LHDNOHDMIMO]
    LKKKDNOHCIG: _containers.RepeatedCompositeFieldContainer[_DOKKNIDHJOB_pb2.DOKKNIDHJOB]
    AMLIJKENIIN: int
    ONKGKHGAFHJ: int
    NJPJCGCNEDO: int
    MPNJAOCKMAH: int
    MONEJDBPOLB: int
    NCPPELGEFPN: bool
    HCJFDJHILAM: bool
    def __init__(self, NEHPGMLDKMF: _Optional[_Iterable[_Union[_LHDNOHDMIMO_pb2.LHDNOHDMIMO, _Mapping]]] = ..., LKKKDNOHCIG: _Optional[_Iterable[_Union[_DOKKNIDHJOB_pb2.DOKKNIDHJOB, _Mapping]]] = ..., AMLIJKENIIN: _Optional[int] = ..., ONKGKHGAFHJ: _Optional[int] = ..., NJPJCGCNEDO: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., MONEJDBPOLB: _Optional[int] = ..., NCPPELGEFPN: bool = ..., HCJFDJHILAM: bool = ...) -> None: ...
