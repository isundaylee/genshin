from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerDieType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYER_DIE_TYPE_NONE: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_KILL_BY_MONSTER: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_KILL_BY_GEAR: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_FALL: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_DRAWN: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_ABYSS: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_GM: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_CLIMATE_COLD: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_STORM_LIGHTING: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_DIRTY_WATER_EROSION: _ClassVar[PlayerDieType]
    PLAYER_DIE_TYPE_LIQUID_PHLOGISTON: _ClassVar[PlayerDieType]
PLAYER_DIE_TYPE_NONE: PlayerDieType
PLAYER_DIE_TYPE_KILL_BY_MONSTER: PlayerDieType
PLAYER_DIE_TYPE_KILL_BY_GEAR: PlayerDieType
PLAYER_DIE_TYPE_FALL: PlayerDieType
PLAYER_DIE_TYPE_DRAWN: PlayerDieType
PLAYER_DIE_TYPE_ABYSS: PlayerDieType
PLAYER_DIE_TYPE_GM: PlayerDieType
PLAYER_DIE_TYPE_CLIMATE_COLD: PlayerDieType
PLAYER_DIE_TYPE_STORM_LIGHTING: PlayerDieType
PLAYER_DIE_TYPE_DIRTY_WATER_EROSION: PlayerDieType
PLAYER_DIE_TYPE_LIQUID_PHLOGISTON: PlayerDieType
