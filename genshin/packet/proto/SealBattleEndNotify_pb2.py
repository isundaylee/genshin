# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SealBattleEndNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/SealBattleEndNotify.proto\"=\n\x13SealBattleEndNotify\x12\x0e\n\x06is_win\x18\x04 \x01(\x08\x12\x16\n\x0eseal_entity_id\x18\x0f \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_SEALBATTLEENDNOTIFY = DESCRIPTOR.message_types_by_name['SealBattleEndNotify']
SealBattleEndNotify = _reflection.GeneratedProtocolMessageType('SealBattleEndNotify', (_message.Message,), {
  'DESCRIPTOR' : _SEALBATTLEENDNOTIFY,
  '__module__' : 'genshin.packet.proto.SealBattleEndNotify_pb2'
  # @@protoc_insertion_point(class_scope:SealBattleEndNotify)
  })
_sym_db.RegisterMessage(SealBattleEndNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SEALBATTLEENDNOTIFY._serialized_start=50
  _SEALBATTLEENDNOTIFY._serialized_end=111
# @@protoc_insertion_point(module_scope)
