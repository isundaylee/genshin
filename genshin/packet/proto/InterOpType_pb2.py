# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/InterOpType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/InterOpType.proto*@\n\x0bInterOpType\x12\x18\n\x14INTER_OP_TYPE_FINISH\x10\x00\x12\x17\n\x13INTER_OP_TYPE_START\x10\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_INTEROPTYPE = DESCRIPTOR.enum_types_by_name['InterOpType']
InterOpType = enum_type_wrapper.EnumTypeWrapper(_INTEROPTYPE)
INTER_OP_TYPE_FINISH = 0
INTER_OP_TYPE_START = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _INTEROPTYPE._serialized_start=42
  _INTEROPTYPE._serialized_end=106
# @@protoc_insertion_point(module_scope)
