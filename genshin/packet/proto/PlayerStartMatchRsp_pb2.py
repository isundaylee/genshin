# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerStartMatchRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MatchType_pb2 as genshin_dot_packet_dot_proto_dot_MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/PlayerStartMatchRsp.proto\x1a$genshin/packet/proto/MatchType.proto\"\xcc\x01\n\x13PlayerStartMatchRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x17\n\x0fpunish_end_time\x18\x05 \x01(\r\x12\r\n\x05param\x18\x04 \x01(\r\x12\x12\n\nmp_play_id\x18\r \x01(\r\x12\"\n\x1amechanicus_difficult_level\x18\x02 \x01(\r\x12\x12\n\ndungeon_id\x18\x03 \x01(\r\x12\x10\n\x08match_id\x18\x08 \x01(\r\x12\x1e\n\nmatch_type\x18\x07 \x01(\x0e\x32\n.MatchTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERSTARTMATCHRSP = DESCRIPTOR.message_types_by_name['PlayerStartMatchRsp']
PlayerStartMatchRsp = _reflection.GeneratedProtocolMessageType('PlayerStartMatchRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTARTMATCHRSP,
  '__module__' : 'genshin.packet.proto.PlayerStartMatchRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerStartMatchRsp)
  })
_sym_db.RegisterMessage(PlayerStartMatchRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERSTARTMATCHRSP._serialized_start=89
  _PLAYERSTARTMATCHRSP._serialized_end=293
# @@protoc_insertion_point(module_scope)
