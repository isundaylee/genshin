# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayProduct.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/PlayProduct.proto\"J\n\x0bPlayProduct\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x12\n\nprice_tier\x18\x02 \x01(\t\x12\x13\n\x0bschedule_id\x18\x03 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYPRODUCT = DESCRIPTOR.message_types_by_name['PlayProduct']
PlayProduct = _reflection.GeneratedProtocolMessageType('PlayProduct', (_message.Message,), {
  'DESCRIPTOR' : _PLAYPRODUCT,
  '__module__' : 'genshin.packet.proto.PlayProduct_pb2'
  # @@protoc_insertion_point(class_scope:PlayProduct)
  })
_sym_db.RegisterMessage(PlayProduct)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYPRODUCT._serialized_start=42
  _PLAYPRODUCT._serialized_end=116
# @@protoc_insertion_point(module_scope)
