# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeBasicInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeBasicInfo_pb2 as genshin_dot_packet_dot_proto_dot_HomeBasicInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/HomeBasicInfoNotify.proto\x1a(genshin/packet/proto/HomeBasicInfo.proto\"9\n\x13HomeBasicInfoNotify\x12\"\n\nbasic_info\x18\x0f \x01(\x0b\x32\x0e.HomeBasicInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEBASICINFONOTIFY = DESCRIPTOR.message_types_by_name['HomeBasicInfoNotify']
HomeBasicInfoNotify = _reflection.GeneratedProtocolMessageType('HomeBasicInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _HOMEBASICINFONOTIFY,
  '__module__' : 'genshin.packet.proto.HomeBasicInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:HomeBasicInfoNotify)
  })
_sym_db.RegisterMessage(HomeBasicInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEBASICINFONOTIFY._serialized_start=92
  _HOMEBASICINFONOTIFY._serialized_end=149
# @@protoc_insertion_point(module_scope)
