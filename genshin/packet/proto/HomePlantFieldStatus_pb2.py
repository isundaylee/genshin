# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomePlantFieldStatus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/HomePlantFieldStatus.proto*\xbe\x01\n\x14HomePlantFieldStatus\x12\'\n#HOME_PLANT_FIELD_STATUS_STATUE_NONE\x10\x00\x12\'\n#HOME_PLANT_FIELD_STATUS_STATUE_SEED\x10\x01\x12)\n%HOME_PLANT_FIELD_STATUS_STATUE_SPROUT\x10\x02\x12)\n%HOME_PLANT_FIELD_STATUS_STATUE_GATHER\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_HOMEPLANTFIELDSTATUS = DESCRIPTOR.enum_types_by_name['HomePlantFieldStatus']
HomePlantFieldStatus = enum_type_wrapper.EnumTypeWrapper(_HOMEPLANTFIELDSTATUS)
HOME_PLANT_FIELD_STATUS_STATUE_NONE = 0
HOME_PLANT_FIELD_STATUS_STATUE_SEED = 1
HOME_PLANT_FIELD_STATUS_STATUE_SPROUT = 2
HOME_PLANT_FIELD_STATUS_STATUE_GATHER = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEPLANTFIELDSTATUS._serialized_start=52
  _HOMEPLANTFIELDSTATUS._serialized_end=242
# @@protoc_insertion_point(module_scope)