# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FriendOnlineState.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/FriendOnlineState.proto*_\n\x11\x46riendOnlineState\x12*\n&FRIEND_ONLINE_STATE_FREIEND_DISCONNECT\x10\x00\x12\x1e\n\x1a\x46RIEND_ONLINE_STATE_ONLINE\x10\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_FRIENDONLINESTATE = DESCRIPTOR.enum_types_by_name['FriendOnlineState']
FriendOnlineState = enum_type_wrapper.EnumTypeWrapper(_FRIENDONLINESTATE)
FRIEND_ONLINE_STATE_FREIEND_DISCONNECT = 0
FRIEND_ONLINE_STATE_ONLINE = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FRIENDONLINESTATE._serialized_start=48
  _FRIENDONLINESTATE._serialized_end=143
# @@protoc_insertion_point(module_scope)
