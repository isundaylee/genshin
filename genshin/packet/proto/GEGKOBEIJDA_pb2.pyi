from genshin.packet.proto import CBGHNFJJJOD_pb2 as _CBGHNFJJJOD_pb2
from genshin.packet.proto import GNIMGOIHNMC_pb2 as _GNIMGOIHNMC_pb2
from genshin.packet.proto import MINGGPMEDIA_pb2 as _MINGGPMEDIA_pb2
from genshin.packet.proto import LKHDONHBJAG_pb2 as _LKHDONHBJAG_pb2
from genshin.packet.proto import CLIIGMPCIDH_pb2 as _CLIIGMPCIDH_pb2
from genshin.packet.proto import KMHHOEPHMJO_pb2 as _KMHHOEPHMJO_pb2
from genshin.packet.proto import PHPOHEGGIMP_pb2 as _PHPOHEGGIMP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GEGKOBEIJDA(_message.Message):
    __slots__ = ("IADFGKJCIDE", "avatar_id", "reliquary_set_request", "element_reliquary_set_request", "weapon_request", "element_reliquary_request", "skill_request", "reliquary_request", "element_weapon_request")
    IADFGKJCIDE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_RELIQUARY_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_RELIQUARY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SKILL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_WEAPON_REQUEST_FIELD_NUMBER: _ClassVar[int]
    IADFGKJCIDE: int
    avatar_id: int
    reliquary_set_request: _CBGHNFJJJOD_pb2.CBGHNFJJJOD
    element_reliquary_set_request: _GNIMGOIHNMC_pb2.GNIMGOIHNMC
    weapon_request: _MINGGPMEDIA_pb2.MINGGPMEDIA
    element_reliquary_request: _LKHDONHBJAG_pb2.LKHDONHBJAG
    skill_request: _CLIIGMPCIDH_pb2.CLIIGMPCIDH
    reliquary_request: _KMHHOEPHMJO_pb2.KMHHOEPHMJO
    element_weapon_request: _PHPOHEGGIMP_pb2.PHPOHEGGIMP
    def __init__(self, IADFGKJCIDE: _Optional[int] = ..., avatar_id: _Optional[int] = ..., reliquary_set_request: _Optional[_Union[_CBGHNFJJJOD_pb2.CBGHNFJJJOD, _Mapping]] = ..., element_reliquary_set_request: _Optional[_Union[_GNIMGOIHNMC_pb2.GNIMGOIHNMC, _Mapping]] = ..., weapon_request: _Optional[_Union[_MINGGPMEDIA_pb2.MINGGPMEDIA, _Mapping]] = ..., element_reliquary_request: _Optional[_Union[_LKHDONHBJAG_pb2.LKHDONHBJAG, _Mapping]] = ..., skill_request: _Optional[_Union[_CLIIGMPCIDH_pb2.CLIIGMPCIDH, _Mapping]] = ..., reliquary_request: _Optional[_Union[_KMHHOEPHMJO_pb2.KMHHOEPHMJO, _Mapping]] = ..., element_weapon_request: _Optional[_Union[_PHPOHEGGIMP_pb2.PHPOHEGGIMP, _Mapping]] = ...) -> None: ...
