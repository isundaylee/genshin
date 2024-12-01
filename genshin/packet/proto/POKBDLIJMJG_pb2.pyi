from genshin.packet.proto import KCICAHCPBGB_pb2 as _KCICAHCPBGB_pb2
from genshin.packet.proto import PMNPLDNDDIP_pb2 as _PMNPLDNDDIP_pb2
from genshin.packet.proto import PLNEFHEEEKB_pb2 as _PLNEFHEEEKB_pb2
from genshin.packet.proto import OLIFCHHIJAG_pb2 as _OLIFCHHIJAG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class POKBDLIJMJG(_message.Message):
    __slots__ = ("AHKCIIMCBOJ", "PLNNILADKMJ", "KPKMLCIGEMN", "EBEPPCGFEGA", "ELONHIAJPEG", "KHCFDEEOMDF", "KIADCANPEPM")
    AHKCIIMCBOJ_FIELD_NUMBER: _ClassVar[int]
    PLNNILADKMJ_FIELD_NUMBER: _ClassVar[int]
    KPKMLCIGEMN_FIELD_NUMBER: _ClassVar[int]
    EBEPPCGFEGA_FIELD_NUMBER: _ClassVar[int]
    ELONHIAJPEG_FIELD_NUMBER: _ClassVar[int]
    KHCFDEEOMDF_FIELD_NUMBER: _ClassVar[int]
    KIADCANPEPM_FIELD_NUMBER: _ClassVar[int]
    AHKCIIMCBOJ: _containers.RepeatedCompositeFieldContainer[_KCICAHCPBGB_pb2.KCICAHCPBGB]
    PLNNILADKMJ: _containers.RepeatedCompositeFieldContainer[_PMNPLDNDDIP_pb2.PMNPLDNDDIP]
    KPKMLCIGEMN: _containers.RepeatedScalarFieldContainer[int]
    EBEPPCGFEGA: _containers.RepeatedScalarFieldContainer[int]
    ELONHIAJPEG: _containers.RepeatedScalarFieldContainer[int]
    KHCFDEEOMDF: _containers.RepeatedCompositeFieldContainer[_PLNEFHEEEKB_pb2.PLNEFHEEEKB]
    KIADCANPEPM: _containers.RepeatedCompositeFieldContainer[_OLIFCHHIJAG_pb2.OLIFCHHIJAG]
    def __init__(self, AHKCIIMCBOJ: _Optional[_Iterable[_Union[_KCICAHCPBGB_pb2.KCICAHCPBGB, _Mapping]]] = ..., PLNNILADKMJ: _Optional[_Iterable[_Union[_PMNPLDNDDIP_pb2.PMNPLDNDDIP, _Mapping]]] = ..., KPKMLCIGEMN: _Optional[_Iterable[int]] = ..., EBEPPCGFEGA: _Optional[_Iterable[int]] = ..., ELONHIAJPEG: _Optional[_Iterable[int]] = ..., KHCFDEEOMDF: _Optional[_Iterable[_Union[_PLNEFHEEEKB_pb2.PLNEFHEEEKB, _Mapping]]] = ..., KIADCANPEPM: _Optional[_Iterable[_Union[_OLIFCHHIJAG_pb2.OLIFCHHIJAG, _Mapping]]] = ...) -> None: ...
