# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MapAreaInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/MapAreaInfo.proto\"3\n\x0bMapAreaInfo\x12\x13\n\x0bmap_area_id\x18\x01 \x01(\r\x12\x0f\n\x07is_open\x18\x02 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MAPAREAINFO = DESCRIPTOR.message_types_by_name['MapAreaInfo']
MapAreaInfo = _reflection.GeneratedProtocolMessageType('MapAreaInfo', (_message.Message,), {
  'DESCRIPTOR' : _MAPAREAINFO,
  '__module__' : 'genshin.packet.proto.MapAreaInfo_pb2'
  # @@protoc_insertion_point(class_scope:MapAreaInfo)
  })
_sym_db.RegisterMessage(MapAreaInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MAPAREAINFO._serialized_start=42
  _MAPAREAINFO._serialized_end=93
# @@protoc_insertion_point(module_scope)