# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/VehicleInteractType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/VehicleInteractType.proto*r\n\x13VehicleInteractType\x12\x1e\n\x1aVEHICLE_INTERACT_TYPE_NONE\x10\x00\x12\x1c\n\x18VEHICLE_INTERACT_TYPE_IN\x10\x01\x12\x1d\n\x19VEHICLE_INTERACT_TYPE_OUT\x10\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_VEHICLEINTERACTTYPE = DESCRIPTOR.enum_types_by_name['VehicleInteractType']
VehicleInteractType = enum_type_wrapper.EnumTypeWrapper(_VEHICLEINTERACTTYPE)
VEHICLE_INTERACT_TYPE_NONE = 0
VEHICLE_INTERACT_TYPE_IN = 1
VEHICLE_INTERACT_TYPE_OUT = 2


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _VEHICLEINTERACTTYPE._serialized_start=50
  _VEHICLEINTERACTTYPE._serialized_end=164
# @@protoc_insertion_point(module_scope)
