# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DealAddFriendResultType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/DealAddFriendResultType.proto*i\n\x17\x44\x65\x61lAddFriendResultType\x12&\n\"DEAL_ADD_FRIEND_RESULT_TYPE_REJECT\x10\x00\x12&\n\"DEAL_ADD_FRIEND_RESULT_TYPE_ACCEPT\x10\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_DEALADDFRIENDRESULTTYPE = DESCRIPTOR.enum_types_by_name['DealAddFriendResultType']
DealAddFriendResultType = enum_type_wrapper.EnumTypeWrapper(_DEALADDFRIENDRESULTTYPE)
DEAL_ADD_FRIEND_RESULT_TYPE_REJECT = 0
DEAL_ADD_FRIEND_RESULT_TYPE_ACCEPT = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DEALADDFRIENDRESULTTYPE._serialized_start=54
  _DEALADDFRIENDRESULTTYPE._serialized_end=159
# @@protoc_insertion_point(module_scope)
