# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeResourceNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeResource_pb2 as genshin_dot_packet_dot_proto_dot_HomeResource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/HomeResourceNotify.proto\x1a\'genshin/packet/proto/HomeResource.proto\"Y\n\x12HomeResourceNotify\x12 \n\thome_coin\x18\t \x01(\x0b\x32\r.HomeResource\x12!\n\nfetter_exp\x18\x08 \x01(\x0b\x32\r.HomeResourceB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMERESOURCENOTIFY = DESCRIPTOR.message_types_by_name['HomeResourceNotify']
HomeResourceNotify = _reflection.GeneratedProtocolMessageType('HomeResourceNotify', (_message.Message,), {
  'DESCRIPTOR' : _HOMERESOURCENOTIFY,
  '__module__' : 'genshin.packet.proto.HomeResourceNotify_pb2'
  # @@protoc_insertion_point(class_scope:HomeResourceNotify)
  })
_sym_db.RegisterMessage(HomeResourceNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMERESOURCENOTIFY._serialized_start=90
  _HOMERESOURCENOTIFY._serialized_end=179
# @@protoc_insertion_point(module_scope)
