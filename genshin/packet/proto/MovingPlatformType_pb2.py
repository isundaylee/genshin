# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MovingPlatformType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/MovingPlatformType.proto*\x9a\x01\n\x12MovingPlatformType\x12\x1d\n\x19MOVING_PLATFORM_TYPE_NONE\x10\x00\x12#\n\x1fMOVING_PLATFORM_TYPE_USE_CONFIG\x10\x01\x12 \n\x1cMOVING_PLATFORM_TYPE_ABILITY\x10\x02\x12\x1e\n\x1aMOVING_PLATFORM_TYPE_ROUTE\x10\x03\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_MOVINGPLATFORMTYPE = DESCRIPTOR.enum_types_by_name['MovingPlatformType']
MovingPlatformType = enum_type_wrapper.EnumTypeWrapper(_MOVINGPLATFORMTYPE)
MOVING_PLATFORM_TYPE_NONE = 0
MOVING_PLATFORM_TYPE_USE_CONFIG = 1
MOVING_PLATFORM_TYPE_ABILITY = 2
MOVING_PLATFORM_TYPE_ROUTE = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MOVINGPLATFORMTYPE._serialized_start=50
  _MOVINGPLATFORMTYPE._serialized_end=204
# @@protoc_insertion_point(module_scope)