# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeMarkPointFurnitureData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeMarkPointNPCData_pb2 as genshin_dot_packet_dot_proto_dot_HomeMarkPointNPCData__pb2
from genshin.packet.proto import HomeMarkPointSuiteData_pb2 as genshin_dot_packet_dot_proto_dot_HomeMarkPointSuiteData__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/HomeMarkPointFurnitureData.proto\x1a/genshin/packet/proto/HomeMarkPointNPCData.proto\x1a\x31genshin/packet/proto/HomeMarkPointSuiteData.proto\x1a!genshin/packet/proto/Vector.proto\"\xd1\x01\n\x1aHomeMarkPointFurnitureData\x12\x0c\n\x04guid\x18\x01 \x01(\r\x12\x14\n\x0c\x66urniture_id\x18\x02 \x01(\r\x12\x16\n\x0e\x66urniture_type\x18\x03 \x01(\r\x12\x14\n\x03pos\x18\x04 \x01(\x0b\x32\x07.Vector\x12)\n\x08npc_data\x18\x06 \x01(\x0b\x32\x15.HomeMarkPointNPCDataH\x00\x12-\n\nsuite_data\x18\x07 \x01(\x0b\x32\x17.HomeMarkPointSuiteDataH\x00\x42\x07\n\x05\x65xtraB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_HOMEMARKPOINTFURNITUREDATA = DESCRIPTOR.message_types_by_name['HomeMarkPointFurnitureData']
HomeMarkPointFurnitureData = _reflection.GeneratedProtocolMessageType('HomeMarkPointFurnitureData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEMARKPOINTFURNITUREDATA,
  '__module__' : 'genshin.packet.proto.HomeMarkPointFurnitureData_pb2'
  # @@protoc_insertion_point(class_scope:HomeMarkPointFurnitureData)
  })
_sym_db.RegisterMessage(HomeMarkPointFurnitureData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _HOMEMARKPOINTFURNITUREDATA._serialized_start=193
  _HOMEMARKPOINTFURNITUREDATA._serialized_end=402
# @@protoc_insertion_point(module_scope)
