# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerMatchInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MatchType_pb2 as genshin_dot_packet_dot_proto_dot_MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/PlayerMatchInfoNotify.proto\x1a$genshin/packet/proto/MatchType.proto\"\xe3\x01\n\x15PlayerMatchInfoNotify\x12\"\n\x1amechanicus_difficult_level\x18\x0c \x01(\r\x12 \n\x18\x65stimate_match_cost_time\x18\x03 \x01(\r\x12\x1e\n\nmatch_type\x18\x0b \x01(\x0e\x32\n.MatchType\x12\x12\n\nmp_play_id\x18\x05 \x01(\r\x12\x10\n\x08match_id\x18\x08 \x01(\r\x12\x18\n\x10match_begin_time\x18\x04 \x01(\r\x12\x12\n\ndungeon_id\x18\n \x01(\r\x12\x10\n\x08host_uid\x18\r \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERMATCHINFONOTIFY = DESCRIPTOR.message_types_by_name['PlayerMatchInfoNotify']
PlayerMatchInfoNotify = _reflection.GeneratedProtocolMessageType('PlayerMatchInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERMATCHINFONOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerMatchInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerMatchInfoNotify)
  })
_sym_db.RegisterMessage(PlayerMatchInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERMATCHINFONOTIFY._serialized_start=91
  _PLAYERMATCHINFONOTIFY._serialized_end=318
# @@protoc_insertion_point(module_scope)
