# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ModifierDurability.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/ModifierDurability.proto\"H\n\x12ModifierDurability\x12\x14\n\x0creduce_ratio\x18\x01 \x01(\x02\x12\x1c\n\x14remaining_durability\x18\x02 \x01(\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MODIFIERDURABILITY = DESCRIPTOR.message_types_by_name['ModifierDurability']
ModifierDurability = _reflection.GeneratedProtocolMessageType('ModifierDurability', (_message.Message,), {
  'DESCRIPTOR' : _MODIFIERDURABILITY,
  '__module__' : 'genshin.packet.proto.ModifierDurability_pb2'
  # @@protoc_insertion_point(class_scope:ModifierDurability)
  })
_sym_db.RegisterMessage(ModifierDurability)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MODIFIERDURABILITY._serialized_start=49
  _MODIFIERDURABILITY._serialized_end=121
# @@protoc_insertion_point(module_scope)
