# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RoguelikeGiveUpRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RoguelikeDungeonSettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_RoguelikeDungeonSettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/RoguelikeGiveUpRsp.proto\x1a\x35genshin/packet/proto/RoguelikeDungeonSettleInfo.proto\"s\n\x12RoguelikeGiveUpRsp\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x12\x10\n\x08stage_id\x18\x07 \x01(\r\x12\x32\n\x0bsettle_info\x18\x08 \x01(\x0b\x32\x1b.RoguelikeDungeonSettleInfoH\x00\x42\x06\n\x04infoB\x16\n\x14org.sorapointa.protob\x06proto3')



_ROGUELIKEGIVEUPRSP = DESCRIPTOR.message_types_by_name['RoguelikeGiveUpRsp']
RoguelikeGiveUpRsp = _reflection.GeneratedProtocolMessageType('RoguelikeGiveUpRsp', (_message.Message,), {
  'DESCRIPTOR' : _ROGUELIKEGIVEUPRSP,
  '__module__' : 'genshin.packet.proto.RoguelikeGiveUpRsp_pb2'
  # @@protoc_insertion_point(class_scope:RoguelikeGiveUpRsp)
  })
_sym_db.RegisterMessage(RoguelikeGiveUpRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ROGUELIKEGIVEUPRSP._serialized_start=104
  _ROGUELIKEGIVEUPRSP._serialized_end=219
# @@protoc_insertion_point(module_scope)
