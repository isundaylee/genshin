# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneRouteChangeInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RoutePointChangeInfo_pb2 as genshin_dot_packet_dot_proto_dot_RoutePointChangeInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/SceneRouteChangeInfo.proto\x1a/genshin/packet/proto/RoutePointChangeInfo.proto\"u\n\x14SceneRouteChangeInfo\x12\x12\n\nis_forward\x18\x0c \x01(\x08\x12\x10\n\x08route_id\x18\x0f \x01(\r\x12\x0c\n\x04type\x18\x04 \x01(\r\x12)\n\npoint_list\x18\x01 \x03(\x0b\x32\x15.RoutePointChangeInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENEROUTECHANGEINFO = DESCRIPTOR.message_types_by_name['SceneRouteChangeInfo']
SceneRouteChangeInfo = _reflection.GeneratedProtocolMessageType('SceneRouteChangeInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENEROUTECHANGEINFO,
  '__module__' : 'genshin.packet.proto.SceneRouteChangeInfo_pb2'
  # @@protoc_insertion_point(class_scope:SceneRouteChangeInfo)
  })
_sym_db.RegisterMessage(SceneRouteChangeInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENEROUTECHANGEINFO._serialized_start=100
  _SCENEROUTECHANGEINFO._serialized_end=217
# @@protoc_insertion_point(module_scope)
