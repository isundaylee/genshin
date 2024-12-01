from genshin.packet.proto import MDKGKHMHLMH_pb2 as _MDKGKHMHLMH_pb2
from genshin.packet.proto import HFFFCNEFIKM_pb2 as _HFFFCNEFIKM_pb2
from genshin.packet.proto import OJIIDHLAOCC_pb2 as _OJIIDHLAOCC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AOPICHBNDLO(_message.Message):
    __slots__ = ("FIBBGLDJHJK", "NPFFLKNKFND", "IMHBPHFPABC", "MPNJAOCKMAH", "AGIDBEEINDE")
    FIBBGLDJHJK_FIELD_NUMBER: _ClassVar[int]
    NPFFLKNKFND_FIELD_NUMBER: _ClassVar[int]
    IMHBPHFPABC_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    FIBBGLDJHJK: _containers.RepeatedCompositeFieldContainer[_MDKGKHMHLMH_pb2.MDKGKHMHLMH]
    NPFFLKNKFND: _HFFFCNEFIKM_pb2.HFFFCNEFIKM
    IMHBPHFPABC: _OJIIDHLAOCC_pb2.OJIIDHLAOCC
    MPNJAOCKMAH: int
    AGIDBEEINDE: int
    def __init__(self, FIBBGLDJHJK: _Optional[_Iterable[_Union[_MDKGKHMHLMH_pb2.MDKGKHMHLMH, _Mapping]]] = ..., NPFFLKNKFND: _Optional[_Union[_HFFFCNEFIKM_pb2.HFFFCNEFIKM, _Mapping]] = ..., IMHBPHFPABC: _Optional[_Union[_OJIIDHLAOCC_pb2.OJIIDHLAOCC, _Mapping]] = ..., MPNJAOCKMAH: _Optional[int] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
