# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FoundationStatus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/FoundationStatus.proto*\x87\x01\n\x10\x46oundationStatus\x12\x1a\n\x16\x46OUNDATION_STATUS_NONE\x10\x00\x12\x1a\n\x16\x46OUNDATION_STATUS_INIT\x10\x01\x12\x1e\n\x1a\x46OUNDATION_STATUS_BUILDING\x10\x02\x12\x1b\n\x17\x46OUNDATION_STATUS_BUILT\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_FOUNDATIONSTATUS = DESCRIPTOR.enum_types_by_name['FoundationStatus']
FoundationStatus = enum_type_wrapper.EnumTypeWrapper(_FOUNDATIONSTATUS)
FOUNDATION_STATUS_NONE = 0
FOUNDATION_STATUS_INIT = 1
FOUNDATION_STATUS_BUILDING = 2
FOUNDATION_STATUS_BUILT = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FOUNDATIONSTATUS._serialized_start=48
  _FOUNDATIONSTATUS._serialized_end=183
# @@protoc_insertion_point(module_scope)
