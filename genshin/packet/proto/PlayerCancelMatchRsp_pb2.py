# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerCancelMatchRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MatchType_pb2 as genshin_dot_packet_dot_proto_dot_MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/PlayerCancelMatchRsp.proto\x1a$genshin/packet/proto/MatchType.proto\"G\n\x14PlayerCancelMatchRsp\x12\x0f\n\x07retcode\x18\x06 \x01(\x05\x12\x1e\n\nmatch_type\x18\x07 \x01(\x0e\x32\n.MatchTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERCANCELMATCHRSP = DESCRIPTOR.message_types_by_name['PlayerCancelMatchRsp']
PlayerCancelMatchRsp = _reflection.GeneratedProtocolMessageType('PlayerCancelMatchRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERCANCELMATCHRSP,
  '__module__' : 'genshin.packet.proto.PlayerCancelMatchRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerCancelMatchRsp)
  })
_sym_db.RegisterMessage(PlayerCancelMatchRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERCANCELMATCHRSP._serialized_start=89
  _PLAYERCANCELMATCHRSP._serialized_end=160
# @@protoc_insertion_point(module_scope)
