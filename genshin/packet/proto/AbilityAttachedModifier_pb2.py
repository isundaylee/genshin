# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityAttachedModifier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/AbilityAttachedModifier.proto\"\x9f\x01\n\x17\x41\x62ilityAttachedModifier\x12\x12\n\nis_invalid\x18\x01 \x01(\x08\x12\x17\n\x0fowner_entity_id\x18\x02 \x01(\r\x12\x1d\n\x15instanced_modifier_id\x18\x03 \x01(\r\x12\x1e\n\x16is_serverbuff_modifier\x18\x04 \x01(\x08\x12\x18\n\x10\x61ttach_name_hash\x18\x05 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ABILITYATTACHEDMODIFIER = DESCRIPTOR.message_types_by_name['AbilityAttachedModifier']
AbilityAttachedModifier = _reflection.GeneratedProtocolMessageType('AbilityAttachedModifier', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYATTACHEDMODIFIER,
  '__module__' : 'genshin.packet.proto.AbilityAttachedModifier_pb2'
  # @@protoc_insertion_point(class_scope:AbilityAttachedModifier)
  })
_sym_db.RegisterMessage(AbilityAttachedModifier)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ABILITYATTACHEDMODIFIER._serialized_start=55
  _ABILITYATTACHEDMODIFIER._serialized_end=214
# @@protoc_insertion_point(module_scope)