# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonCandidateTeamPlayerLeaveReason.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@genshin/packet/proto/DungeonCandidateTeamPlayerLeaveReason.proto*\x94\x02\n%DungeonCandidateTeamPlayerLeaveReason\x12:\n6DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_NORMAL\x10\x00\x12\x37\n3DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_DIE\x10\x01\x12;\n7DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_BE_KICK\x10\x02\x12\x39\n5DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_DISCONNECT\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_DUNGEONCANDIDATETEAMPLAYERLEAVEREASON = DESCRIPTOR.enum_types_by_name['DungeonCandidateTeamPlayerLeaveReason']
DungeonCandidateTeamPlayerLeaveReason = enum_type_wrapper.EnumTypeWrapper(_DUNGEONCANDIDATETEAMPLAYERLEAVEREASON)
DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_NORMAL = 0
DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_DIE = 1
DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_TPLR_BE_KICK = 2
DUNGEON_CANDIDATE_TEAM_PLAYER_LEAVE_REASON_DISCONNECT = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DUNGEONCANDIDATETEAMPLAYERLEAVEREASON._serialized_start=69
  _DUNGEONCANDIDATETEAMPLAYERLEAVEREASON._serialized_end=345
# @@protoc_insertion_point(module_scope)
