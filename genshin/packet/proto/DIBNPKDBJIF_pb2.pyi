from genshin.packet.proto import NCDNMMMMKAF_pb2 as _NCDNMMMMKAF_pb2
from genshin.packet.proto import NEBCILHOAHF_pb2 as _NEBCILHOAHF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DIBNPKDBJIF(_message.Message):
    __slots__ = ("MFAIOELAMEC", "HAEFDCKNFOI", "BJEIPHDHNHO", "GEMAGMEFCCG", "NEFCDAAILEO")
    MFAIOELAMEC_FIELD_NUMBER: _ClassVar[int]
    HAEFDCKNFOI_FIELD_NUMBER: _ClassVar[int]
    BJEIPHDHNHO_FIELD_NUMBER: _ClassVar[int]
    GEMAGMEFCCG_FIELD_NUMBER: _ClassVar[int]
    NEFCDAAILEO_FIELD_NUMBER: _ClassVar[int]
    MFAIOELAMEC: _NCDNMMMMKAF_pb2.NCDNMMMMKAF
    HAEFDCKNFOI: _NEBCILHOAHF_pb2.NEBCILHOAHF
    BJEIPHDHNHO: int
    GEMAGMEFCCG: int
    NEFCDAAILEO: int
    def __init__(self, MFAIOELAMEC: _Optional[_Union[_NCDNMMMMKAF_pb2.NCDNMMMMKAF, _Mapping]] = ..., HAEFDCKNFOI: _Optional[_Union[_NEBCILHOAHF_pb2.NEBCILHOAHF, _Mapping]] = ..., BJEIPHDHNHO: _Optional[int] = ..., GEMAGMEFCCG: _Optional[int] = ..., NEFCDAAILEO: _Optional[int] = ...) -> None: ...
