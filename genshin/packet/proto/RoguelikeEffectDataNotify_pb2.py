# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RoguelikeEffectDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RogueEffectRecord_pb2 as genshin_dot_packet_dot_proto_dot_RogueEffectRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/RoguelikeEffectDataNotify.proto\x1a,genshin/packet/proto/RogueEffectRecord.proto\"j\n\x19RoguelikeEffectDataNotify\x12&\n\ncurse_list\x18\x07 \x03(\x0b\x32\x12.RogueEffectRecord\x12%\n\tcard_list\x18\x04 \x03(\x0b\x32\x12.RogueEffectRecordB\x16\n\x14org.sorapointa.protob\x06proto3')



_ROGUELIKEEFFECTDATANOTIFY = DESCRIPTOR.message_types_by_name['RoguelikeEffectDataNotify']
RoguelikeEffectDataNotify = _reflection.GeneratedProtocolMessageType('RoguelikeEffectDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _ROGUELIKEEFFECTDATANOTIFY,
  '__module__' : 'genshin.packet.proto.RoguelikeEffectDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:RoguelikeEffectDataNotify)
  })
_sym_db.RegisterMessage(RoguelikeEffectDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ROGUELIKEEFFECTDATANOTIFY._serialized_start=102
  _ROGUELIKEEFFECTDATANOTIFY._serialized_end=208
# @@protoc_insertion_point(module_scope)