# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FleurFairStageSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FleurFairBossSettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_FleurFairBossSettleInfo__pb2
from genshin.packet.proto import FleurFairGallerySettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_FleurFairGallerySettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/FleurFairStageSettleNotify.proto\x1a\x32genshin/packet/proto/FleurFairBossSettleInfo.proto\x1a\x35genshin/packet/proto/FleurFairGallerySettleInfo.proto\"\xac\x01\n\x1a\x46leurFairStageSettleNotify\x12\x12\n\nstage_type\x18\n \x01(\r\x12:\n\x13gallery_settle_info\x18\r \x01(\x0b\x32\x1b.FleurFairGallerySettleInfoH\x00\x12\x34\n\x10\x62oss_settle_info\x18\x0e \x01(\x0b\x32\x18.FleurFairBossSettleInfoH\x00\x42\x08\n\x06\x64\x65tailB\x16\n\x14org.sorapointa.protob\x06proto3')



_FLEURFAIRSTAGESETTLENOTIFY = DESCRIPTOR.message_types_by_name['FleurFairStageSettleNotify']
FleurFairStageSettleNotify = _reflection.GeneratedProtocolMessageType('FleurFairStageSettleNotify', (_message.Message,), {
  'DESCRIPTOR' : _FLEURFAIRSTAGESETTLENOTIFY,
  '__module__' : 'genshin.packet.proto.FleurFairStageSettleNotify_pb2'
  # @@protoc_insertion_point(class_scope:FleurFairStageSettleNotify)
  })
_sym_db.RegisterMessage(FleurFairStageSettleNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FLEURFAIRSTAGESETTLENOTIFY._serialized_start=165
  _FLEURFAIRSTAGESETTLENOTIFY._serialized_end=337
# @@protoc_insertion_point(module_scope)
