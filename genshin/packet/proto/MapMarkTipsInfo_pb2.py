# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MapMarkTipsInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MapMarkTipsType_pb2 as genshin_dot_packet_dot_proto_dot_MapMarkTipsType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/MapMarkTipsInfo.proto\x1a*genshin/packet/proto/MapMarkTipsType.proto\"M\n\x0fMapMarkTipsInfo\x12#\n\ttips_type\x18\x01 \x01(\x0e\x32\x10.MapMarkTipsType\x12\x15\n\rpoint_id_list\x18\x02 \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_MAPMARKTIPSINFO = DESCRIPTOR.message_types_by_name['MapMarkTipsInfo']
MapMarkTipsInfo = _reflection.GeneratedProtocolMessageType('MapMarkTipsInfo', (_message.Message,), {
  'DESCRIPTOR' : _MAPMARKTIPSINFO,
  '__module__' : 'genshin.packet.proto.MapMarkTipsInfo_pb2'
  # @@protoc_insertion_point(class_scope:MapMarkTipsInfo)
  })
_sym_db.RegisterMessage(MapMarkTipsInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MAPMARKTIPSINFO._serialized_start=90
  _MAPMARKTIPSINFO._serialized_end=167
# @@protoc_insertion_point(module_scope)
