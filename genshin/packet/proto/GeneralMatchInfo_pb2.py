# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GeneralMatchInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MatchPlayerInfo_pb2 as genshin_dot_packet_dot_proto_dot_MatchPlayerInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/GeneralMatchInfo.proto\x1a*genshin/packet/proto/MatchPlayerInfo.proto\"`\n\x10GeneralMatchInfo\x12\x13\n\x0bmatch_param\x18\x01 \x01(\r\x12\x10\n\x08match_id\x18\t \x01(\r\x12%\n\x0bplayer_list\x18\x05 \x03(\x0b\x32\x10.MatchPlayerInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_GENERALMATCHINFO = DESCRIPTOR.message_types_by_name['GeneralMatchInfo']
GeneralMatchInfo = _reflection.GeneratedProtocolMessageType('GeneralMatchInfo', (_message.Message,), {
  'DESCRIPTOR' : _GENERALMATCHINFO,
  '__module__' : 'genshin.packet.proto.GeneralMatchInfo_pb2'
  # @@protoc_insertion_point(class_scope:GeneralMatchInfo)
  })
_sym_db.RegisterMessage(GeneralMatchInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GENERALMATCHINFO._serialized_start=91
  _GENERALMATCHINFO._serialized_end=187
# @@protoc_insertion_point(module_scope)
