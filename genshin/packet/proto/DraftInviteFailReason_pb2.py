# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DraftInviteFailReason.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/DraftInviteFailReason.proto*\xae\x02\n\x15\x44raftInviteFailReason\x12$\n DRAFT_INVITE_FAIL_REASON_UNKNOWN\x10\x00\x12.\n*DRAFT_INVITE_FAIL_REASON_ACTIVITY_NOT_OPEN\x10\x01\x12\x33\n/DRAFT_INVITE_FAIL_REASON_ACTIVITY_PLAY_NOT_OPEN\x10\x02\x12+\n\'DRAFT_INVITE_FAIL_REASON_SCENE_NOT_MEET\x10\x03\x12+\n\'DRAFT_INVITE_FAIL_REASON_WORLD_NOT_MEET\x10\x04\x12\x30\n,DRAFT_INVITE_FAIL_REASON_PLAY_LIMIT_NOT_MEET\x10\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_DRAFTINVITEFAILREASON = DESCRIPTOR.enum_types_by_name['DraftInviteFailReason']
DraftInviteFailReason = enum_type_wrapper.EnumTypeWrapper(_DRAFTINVITEFAILREASON)
DRAFT_INVITE_FAIL_REASON_UNKNOWN = 0
DRAFT_INVITE_FAIL_REASON_ACTIVITY_NOT_OPEN = 1
DRAFT_INVITE_FAIL_REASON_ACTIVITY_PLAY_NOT_OPEN = 2
DRAFT_INVITE_FAIL_REASON_SCENE_NOT_MEET = 3
DRAFT_INVITE_FAIL_REASON_WORLD_NOT_MEET = 4
DRAFT_INVITE_FAIL_REASON_PLAY_LIMIT_NOT_MEET = 5


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DRAFTINVITEFAILREASON._serialized_start=53
  _DRAFTINVITEFAILREASON._serialized_end=355
# @@protoc_insertion_point(module_scope)
