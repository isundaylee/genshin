# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AllCoopInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MainCoop_pb2 as genshin_dot_packet_dot_proto_dot_MainCoop__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/AllCoopInfoNotify.proto\x1a#genshin/packet/proto/MainCoop.proto\"6\n\x11\x41llCoopInfoNotify\x12!\n\x0emain_coop_list\x18\x0e \x03(\x0b\x32\t.MainCoopB\x16\n\x14org.sorapointa.protob\x06proto3')



_ALLCOOPINFONOTIFY = DESCRIPTOR.message_types_by_name['AllCoopInfoNotify']
AllCoopInfoNotify = _reflection.GeneratedProtocolMessageType('AllCoopInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _ALLCOOPINFONOTIFY,
  '__module__' : 'genshin.packet.proto.AllCoopInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:AllCoopInfoNotify)
  })
_sym_db.RegisterMessage(AllCoopInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ALLCOOPINFONOTIFY._serialized_start=85
  _ALLCOOPINFONOTIFY._serialized_end=139
# @@protoc_insertion_point(module_scope)
