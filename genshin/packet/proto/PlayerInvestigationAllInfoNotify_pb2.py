# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerInvestigationAllInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Investigation_pb2 as genshin_dot_packet_dot_proto_dot_Investigation__pb2
from genshin.packet.proto import InvestigationTarget_pb2 as genshin_dot_packet_dot_proto_dot_InvestigationTarget__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;genshin/packet/proto/PlayerInvestigationAllInfoNotify.proto\x1a(genshin/packet/proto/Investigation.proto\x1a.genshin/packet/proto/InvestigationTarget.proto\"\x87\x01\n PlayerInvestigationAllInfoNotify\x12*\n\x12investigation_list\x18\x0f \x03(\x0b\x32\x0e.Investigation\x12\x37\n\x19investigation_target_list\x18\x0c \x03(\x0b\x32\x14.InvestigationTargetB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERINVESTIGATIONALLINFONOTIFY = DESCRIPTOR.message_types_by_name['PlayerInvestigationAllInfoNotify']
PlayerInvestigationAllInfoNotify = _reflection.GeneratedProtocolMessageType('PlayerInvestigationAllInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERINVESTIGATIONALLINFONOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerInvestigationAllInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerInvestigationAllInfoNotify)
  })
_sym_db.RegisterMessage(PlayerInvestigationAllInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERINVESTIGATIONALLINFONOTIFY._serialized_start=154
  _PLAYERINVESTIGATIONALLINFONOTIFY._serialized_end=289
# @@protoc_insertion_point(module_scope)
