# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Route.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RoutePoint_pb2 as genshin_dot_packet_dot_proto_dot_RoutePoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n genshin/packet/proto/Route.proto\x1a%genshin/packet/proto/RoutePoint.proto\">\n\x05Route\x12!\n\x0croute_points\x18\x01 \x03(\x0b\x32\x0b.RoutePoint\x12\x12\n\nroute_type\x18\x02 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ROUTE = DESCRIPTOR.message_types_by_name['Route']
Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
  'DESCRIPTOR' : _ROUTE,
  '__module__' : 'genshin.packet.proto.Route_pb2'
  # @@protoc_insertion_point(class_scope:Route)
  })
_sym_db.RegisterMessage(Route)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ROUTE._serialized_start=75
  _ROUTE._serialized_end=137
# @@protoc_insertion_point(module_scope)
