# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerDieType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/PlayerDieType.proto*\x9e\x02\n\rPlayerDieType\x12\x18\n\x14PLAYER_DIE_TYPE_NONE\x10\x00\x12#\n\x1fPLAYER_DIE_TYPE_KILL_BY_MONSTER\x10\x01\x12 \n\x1cPLAYER_DIE_TYPE_KILL_BY_GEAR\x10\x02\x12\x18\n\x14PLAYER_DIE_TYPE_FALL\x10\x03\x12\x19\n\x15PLAYER_DIE_TYPE_DRAWN\x10\x04\x12\x19\n\x15PLAYER_DIE_TYPE_ABYSS\x10\x05\x12\x16\n\x12PLAYER_DIE_TYPE_GM\x10\x06\x12 \n\x1cPLAYER_DIE_TYPE_CLIMATE_COLD\x10\x07\x12\"\n\x1ePLAYER_DIE_TYPE_STORM_LIGHTING\x10\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_PLAYERDIETYPE = DESCRIPTOR.enum_types_by_name['PlayerDieType']
PlayerDieType = enum_type_wrapper.EnumTypeWrapper(_PLAYERDIETYPE)
PLAYER_DIE_TYPE_NONE = 0
PLAYER_DIE_TYPE_KILL_BY_MONSTER = 1
PLAYER_DIE_TYPE_KILL_BY_GEAR = 2
PLAYER_DIE_TYPE_FALL = 3
PLAYER_DIE_TYPE_DRAWN = 4
PLAYER_DIE_TYPE_ABYSS = 5
PLAYER_DIE_TYPE_GM = 6
PLAYER_DIE_TYPE_CLIMATE_COLD = 7
PLAYER_DIE_TYPE_STORM_LIGHTING = 8


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERDIETYPE._serialized_start=45
  _PLAYERDIETYPE._serialized_end=331
# @@protoc_insertion_point(module_scope)
