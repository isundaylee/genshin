# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CoopPointState.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/CoopPointState.proto*:\n\x0e\x43oopPointState\x12\r\n\tUnstarted\x10\x00\x12\x0b\n\x07Started\x10\x01\x12\x0c\n\x08\x46inished\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_COOPPOINTSTATE = DESCRIPTOR.enum_types_by_name['CoopPointState']
CoopPointState = enum_type_wrapper.EnumTypeWrapper(_COOPPOINTSTATE)
Unstarted = 0
Started = 1
Finished = 2


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _COOPPOINTSTATE._serialized_start=45
  _COOPPOINTSTATE._serialized_end=103
# @@protoc_insertion_point(module_scope)
