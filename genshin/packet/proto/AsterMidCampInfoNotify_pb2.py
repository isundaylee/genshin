# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AsterMidCampInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AsterMidCampInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterMidCampInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/AsterMidCampInfoNotify.proto\x1a+genshin/packet/proto/AsterMidCampInfo.proto\">\n\x16\x41sterMidCampInfoNotify\x12$\n\tcamp_list\x18\x05 \x03(\x0b\x32\x11.AsterMidCampInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_ASTERMIDCAMPINFONOTIFY = DESCRIPTOR.message_types_by_name['AsterMidCampInfoNotify']
AsterMidCampInfoNotify = _reflection.GeneratedProtocolMessageType('AsterMidCampInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _ASTERMIDCAMPINFONOTIFY,
  '__module__' : 'genshin.packet.proto.AsterMidCampInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:AsterMidCampInfoNotify)
  })
_sym_db.RegisterMessage(AsterMidCampInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ASTERMIDCAMPINFONOTIFY._serialized_start=98
  _ASTERMIDCAMPINFONOTIFY._serialized_end=160
# @@protoc_insertion_point(module_scope)