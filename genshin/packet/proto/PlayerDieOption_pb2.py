# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerDieOption.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/PlayerDieOption.proto*\x97\x01\n\x0fPlayerDieOption\x12\x1e\n\x1aPLAYER_DIE_OPTION_OPT_NONE\x10\x00\x12 \n\x1cPLAYER_DIE_OPTION_OPT_REPLAY\x10\x01\x12 \n\x1cPLAYER_DIE_OPTION_OPT_CANCEL\x10\x02\x12 \n\x1cPLAYER_DIE_OPTION_OPT_REVIVE\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_PLAYERDIEOPTION = DESCRIPTOR.enum_types_by_name['PlayerDieOption']
PlayerDieOption = enum_type_wrapper.EnumTypeWrapper(_PLAYERDIEOPTION)
PLAYER_DIE_OPTION_OPT_NONE = 0
PLAYER_DIE_OPTION_OPT_REPLAY = 1
PLAYER_DIE_OPTION_OPT_CANCEL = 2
PLAYER_DIE_OPTION_OPT_REVIVE = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERDIEOPTION._serialized_start=47
  _PLAYERDIEOPTION._serialized_end=198
# @@protoc_insertion_point(module_scope)
