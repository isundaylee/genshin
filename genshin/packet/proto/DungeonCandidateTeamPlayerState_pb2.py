# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonCandidateTeamPlayerState.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:genshin/packet/proto/DungeonCandidateTeamPlayerState.proto*\xb7\x01\n\x1f\x44ungeonCandidateTeamPlayerState\x12,\n(DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_IDLE\x10\x00\x12\x37\n3DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_CHANGING_AVATAR\x10\x01\x12-\n)DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_READY\x10\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_DUNGEONCANDIDATETEAMPLAYERSTATE = DESCRIPTOR.enum_types_by_name['DungeonCandidateTeamPlayerState']
DungeonCandidateTeamPlayerState = enum_type_wrapper.EnumTypeWrapper(_DUNGEONCANDIDATETEAMPLAYERSTATE)
DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_IDLE = 0
DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_CHANGING_AVATAR = 1
DUNGEON_CANDIDATE_TEAM_PLAYER_STATE_READY = 2


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DUNGEONCANDIDATETEAMPLAYERSTATE._serialized_start=63
  _DUNGEONCANDIDATETEAMPLAYERSTATE._serialized_end=246
# @@protoc_insertion_point(module_scope)