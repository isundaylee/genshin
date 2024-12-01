from genshin.packet.proto import AFAPLAEFBIL_pb2 as _AFAPLAEFBIL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOJADOADKGD(_message.Message):
    __slots__ = ("APLPJPOKLAG", "OPOOBJEOOKM", "KLJCAGKGILP", "HPODKDCCIKJ", "MBBKAENBCKD")
    APLPJPOKLAG_FIELD_NUMBER: _ClassVar[int]
    OPOOBJEOOKM_FIELD_NUMBER: _ClassVar[int]
    KLJCAGKGILP_FIELD_NUMBER: _ClassVar[int]
    HPODKDCCIKJ_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    APLPJPOKLAG: int
    OPOOBJEOOKM: _AFAPLAEFBIL_pb2.AFAPLAEFBIL
    KLJCAGKGILP: int
    HPODKDCCIKJ: int
    MBBKAENBCKD: int
    def __init__(self, APLPJPOKLAG: _Optional[int] = ..., OPOOBJEOOKM: _Optional[_Union[_AFAPLAEFBIL_pb2.AFAPLAEFBIL, str]] = ..., KLJCAGKGILP: _Optional[int] = ..., HPODKDCCIKJ: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ...) -> None: ...
