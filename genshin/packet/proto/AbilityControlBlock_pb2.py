# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityControlBlock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityEmbryo_pb2 as genshin_dot_packet_dot_proto_dot_AbilityEmbryo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/AbilityControlBlock.proto\x1a(genshin/packet/proto/AbilityEmbryo.proto\"B\n\x13\x41\x62ilityControlBlock\x12+\n\x13\x61\x62ility_embryo_list\x18\x01 \x03(\x0b\x32\x0e.AbilityEmbryoB\x16\n\x14org.sorapointa.protob\x06proto3')



_ABILITYCONTROLBLOCK = DESCRIPTOR.message_types_by_name['AbilityControlBlock']
AbilityControlBlock = _reflection.GeneratedProtocolMessageType('AbilityControlBlock', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYCONTROLBLOCK,
  '__module__' : 'genshin.packet.proto.AbilityControlBlock_pb2'
  # @@protoc_insertion_point(class_scope:AbilityControlBlock)
  })
_sym_db.RegisterMessage(AbilityControlBlock)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ABILITYCONTROLBLOCK._serialized_start=92
  _ABILITYCONTROLBLOCK._serialized_end=158
# @@protoc_insertion_point(module_scope)
