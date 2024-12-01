from genshin.packet.proto import AINOMEBMCND_pb2 as _AINOMEBMCND_pb2
from genshin.packet.proto import JOECMEMNPFA_pb2 as _JOECMEMNPFA_pb2
from genshin.packet.proto import JIIEFLHJODE_pb2 as _JIIEFLHJODE_pb2
from genshin.packet.proto import AABBEIIFPED_pb2 as _AABBEIIFPED_pb2
from genshin.packet.proto import DDLCCIFIIMC_pb2 as _DDLCCIFIIMC_pb2
from genshin.packet.proto import KHFHHGCMAKK_pb2 as _KHFHHGCMAKK_pb2
from genshin.packet.proto import FGFCBNJMMIA_pb2 as _FGFCBNJMMIA_pb2
from genshin.packet.proto import BEOBMOMNCMK_pb2 as _BEOBMOMNCMK_pb2
from genshin.packet.proto import JICMPNOJHLI_pb2 as _JICMPNOJHLI_pb2
from genshin.packet.proto import FOGEJOFFJPP_pb2 as _FOGEJOFFJPP_pb2
from genshin.packet.proto import AFMDLHNNBEL_pb2 as _AFMDLHNNBEL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JNEBBAFFGPJ(_message.Message):
    __slots__ = ("op_attack", "op_reroll", "op_select_on_stage", "op_redraw", "op_discover", "op_reboot", "op_surrender", "op_play_card", "op_vehicle", "op_change_character_index", "op_pass")
    OP_ATTACK_FIELD_NUMBER: _ClassVar[int]
    OP_REROLL_FIELD_NUMBER: _ClassVar[int]
    OP_SELECT_ON_STAGE_FIELD_NUMBER: _ClassVar[int]
    OP_REDRAW_FIELD_NUMBER: _ClassVar[int]
    OP_DISCOVER_FIELD_NUMBER: _ClassVar[int]
    OP_REBOOT_FIELD_NUMBER: _ClassVar[int]
    OP_SURRENDER_FIELD_NUMBER: _ClassVar[int]
    OP_PLAY_CARD_FIELD_NUMBER: _ClassVar[int]
    OP_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    OP_CHANGE_CHARACTER_INDEX_FIELD_NUMBER: _ClassVar[int]
    OP_PASS_FIELD_NUMBER: _ClassVar[int]
    op_attack: _AINOMEBMCND_pb2.AINOMEBMCND
    op_reroll: _JOECMEMNPFA_pb2.JOECMEMNPFA
    op_select_on_stage: _JIIEFLHJODE_pb2.JIIEFLHJODE
    op_redraw: _AABBEIIFPED_pb2.AABBEIIFPED
    op_discover: _DDLCCIFIIMC_pb2.DDLCCIFIIMC
    op_reboot: _KHFHHGCMAKK_pb2.KHFHHGCMAKK
    op_surrender: _FGFCBNJMMIA_pb2.FGFCBNJMMIA
    op_play_card: _BEOBMOMNCMK_pb2.BEOBMOMNCMK
    op_vehicle: _JICMPNOJHLI_pb2.JICMPNOJHLI
    op_change_character_index: _FOGEJOFFJPP_pb2.FOGEJOFFJPP
    op_pass: _AFMDLHNNBEL_pb2.AFMDLHNNBEL
    def __init__(self, op_attack: _Optional[_Union[_AINOMEBMCND_pb2.AINOMEBMCND, _Mapping]] = ..., op_reroll: _Optional[_Union[_JOECMEMNPFA_pb2.JOECMEMNPFA, _Mapping]] = ..., op_select_on_stage: _Optional[_Union[_JIIEFLHJODE_pb2.JIIEFLHJODE, _Mapping]] = ..., op_redraw: _Optional[_Union[_AABBEIIFPED_pb2.AABBEIIFPED, _Mapping]] = ..., op_discover: _Optional[_Union[_DDLCCIFIIMC_pb2.DDLCCIFIIMC, _Mapping]] = ..., op_reboot: _Optional[_Union[_KHFHHGCMAKK_pb2.KHFHHGCMAKK, _Mapping]] = ..., op_surrender: _Optional[_Union[_FGFCBNJMMIA_pb2.FGFCBNJMMIA, _Mapping]] = ..., op_play_card: _Optional[_Union[_BEOBMOMNCMK_pb2.BEOBMOMNCMK, _Mapping]] = ..., op_vehicle: _Optional[_Union[_JICMPNOJHLI_pb2.JICMPNOJHLI, _Mapping]] = ..., op_change_character_index: _Optional[_Union[_FOGEJOFFJPP_pb2.FOGEJOFFJPP, _Mapping]] = ..., op_pass: _Optional[_Union[_AFMDLHNNBEL_pb2.AFMDLHNNBEL, _Mapping]] = ...) -> None: ...
