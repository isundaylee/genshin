# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PolygonRegionSize.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import VectorPlane_pb2 as genshin_dot_packet_dot_proto_dot_VectorPlane__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/PolygonRegionSize.proto\x1a&genshin/packet/proto/VectorPlane.proto\"E\n\x11PolygonRegionSize\x12 \n\npoint_list\x18\x05 \x03(\x0b\x32\x0c.VectorPlane\x12\x0e\n\x06height\x18\t \x01(\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_POLYGONREGIONSIZE = DESCRIPTOR.message_types_by_name['PolygonRegionSize']
PolygonRegionSize = _reflection.GeneratedProtocolMessageType('PolygonRegionSize', (_message.Message,), {
  'DESCRIPTOR' : _POLYGONREGIONSIZE,
  '__module__' : 'genshin.packet.proto.PolygonRegionSize_pb2'
  # @@protoc_insertion_point(class_scope:PolygonRegionSize)
  })
_sym_db.RegisterMessage(PolygonRegionSize)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _POLYGONREGIONSIZE._serialized_start=88
  _POLYGONREGIONSIZE._serialized_end=157
# @@protoc_insertion_point(module_scope)