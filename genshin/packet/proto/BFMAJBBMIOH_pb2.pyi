from genshin.packet.proto import BCDOMHBDHAJ_pb2 as _BCDOMHBDHAJ_pb2
from genshin.packet.proto import MNHBEHENECP_pb2 as _MNHBEHENECP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BFMAJBBMIOH(_message.Message):
    __slots__ = ("BNACCMFLPKO", "ICIDPJHBDJI", "score_challenge_info", "bundle_info", "boss_challenge_id")
    BNACCMFLPKO_FIELD_NUMBER: _ClassVar[int]
    ICIDPJHBDJI_FIELD_NUMBER: _ClassVar[int]
    SCORE_CHALLENGE_INFO_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_INFO_FIELD_NUMBER: _ClassVar[int]
    BOSS_CHALLENGE_ID_FIELD_NUMBER: _ClassVar[int]
    BNACCMFLPKO: bool
    ICIDPJHBDJI: int
    score_challenge_info: _BCDOMHBDHAJ_pb2.BCDOMHBDHAJ
    bundle_info: _MNHBEHENECP_pb2.MNHBEHENECP
    boss_challenge_id: int
    def __init__(self, BNACCMFLPKO: bool = ..., ICIDPJHBDJI: _Optional[int] = ..., score_challenge_info: _Optional[_Union[_BCDOMHBDHAJ_pb2.BCDOMHBDHAJ, _Mapping]] = ..., bundle_info: _Optional[_Union[_MNHBEHENECP_pb2.MNHBEHENECP, _Mapping]] = ..., boss_challenge_id: _Optional[int] = ...) -> None: ...
