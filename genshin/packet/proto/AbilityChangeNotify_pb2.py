# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityControlBlock_pb2 as genshin_dot_packet_dot_proto_dot_AbilityControlBlock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/AbilityChangeNotify.proto\x1a.genshin/packet/proto/AbilityControlBlock.proto\"]\n\x13\x41\x62ilityChangeNotify\x12\x11\n\tentity_id\x18\x01 \x01(\r\x12\x33\n\x15\x61\x62ility_control_block\x18\x0f \x01(\x0b\x32\x14.AbilityControlBlockB\x16\n\x14org.sorapointa.protob\x06proto3')



_ABILITYCHANGENOTIFY = DESCRIPTOR.message_types_by_name['AbilityChangeNotify']
AbilityChangeNotify = _reflection.GeneratedProtocolMessageType('AbilityChangeNotify', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.AbilityChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:AbilityChangeNotify)
  })
_sym_db.RegisterMessage(AbilityChangeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ABILITYCHANGENOTIFY._serialized_start=98
  _ABILITYCHANGENOTIFY._serialized_end=191
# @@protoc_insertion_point(module_scope)
