# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlatformChangeRouteNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlatformInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlatformInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/PlatformChangeRouteNotify.proto\x1a\'genshin/packet/proto/PlatformInfo.proto\"c\n\x19PlatformChangeRouteNotify\x12\x11\n\tentity_id\x18\x02 \x01(\r\x12\x1f\n\x08platform\x18\x01 \x01(\x0b\x32\r.PlatformInfo\x12\x12\n\nscene_time\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLATFORMCHANGEROUTENOTIFY = DESCRIPTOR.message_types_by_name['PlatformChangeRouteNotify']
PlatformChangeRouteNotify = _reflection.GeneratedProtocolMessageType('PlatformChangeRouteNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLATFORMCHANGEROUTENOTIFY,
  '__module__' : 'genshin.packet.proto.PlatformChangeRouteNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlatformChangeRouteNotify)
  })
_sym_db.RegisterMessage(PlatformChangeRouteNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLATFORMCHANGEROUTENOTIFY._serialized_start=97
  _PLATFORMCHANGEROUTENOTIFY._serialized_end=196
# @@protoc_insertion_point(module_scope)