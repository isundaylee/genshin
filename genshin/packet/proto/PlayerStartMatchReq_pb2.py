# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerStartMatchReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MatchType_pb2 as genshin_dot_packet_dot_proto_dot_MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/PlayerStartMatchReq.proto\x1a$genshin/packet/proto/MatchType.proto\"\xad\x01\n\x13PlayerStartMatchReq\x12\x1e\n\nmatch_type\x18\x03 \x01(\x0e\x32\n.MatchType\x12\"\n\x1amechanicus_difficult_level\x18\x0c \x01(\r\x12\x18\n\x10match_param_list\x18\x0b \x03(\r\x12\x12\n\ndungeon_id\x18\x01 \x01(\r\x12\x12\n\nmp_play_id\x18\x0f \x01(\r\x12\x10\n\x08match_id\x18\x06 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERSTARTMATCHREQ = DESCRIPTOR.message_types_by_name['PlayerStartMatchReq']
PlayerStartMatchReq = _reflection.GeneratedProtocolMessageType('PlayerStartMatchReq', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTARTMATCHREQ,
  '__module__' : 'genshin.packet.proto.PlayerStartMatchReq_pb2'
  # @@protoc_insertion_point(class_scope:PlayerStartMatchReq)
  })
_sym_db.RegisterMessage(PlayerStartMatchReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERSTARTMATCHREQ._serialized_start=89
  _PLAYERSTARTMATCHREQ._serialized_end=262
# @@protoc_insertion_point(module_scope)