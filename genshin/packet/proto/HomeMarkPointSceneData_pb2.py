# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeMarkPointSceneData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeMarkPointFurnitureData_pb2 as genshin_dot_packet_dot_proto_dot_HomeMarkPointFurnitureData__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/HomeMarkPointSceneData.proto\x1a\x35genshin/packet/proto/HomeMarkPointFurnitureData.proto\x1a!genshin/packet/proto/Vector.proto\"\xbc\x01\n\x16HomeMarkPointSceneData\x12\x33\n\x0e\x66urniture_list\x18\x06 \x03(\x0b\x32\x1b.HomeMarkPointFurnitureData\x12\"\n\x11teapot_spirit_pos\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x10\n\x08scene_id\x18\x02 \x01(\r\x12\x11\n\tmodule_id\x18\x05 \x01(\r\x12$\n\x13Unk3100_ABBFBELGECB\x18\x0b \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEMARKPOINTSCENEDATA = DESCRIPTOR.message_types_by_name['HomeMarkPointSceneData']
HomeMarkPointSceneData = _reflection.GeneratedProtocolMessageType('HomeMarkPointSceneData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEMARKPOINTSCENEDATA,
  '__module__' : 'genshin.packet.proto.HomeMarkPointSceneData_pb2'
  # @@protoc_insertion_point(class_scope:HomeMarkPointSceneData)
  })
_sym_db.RegisterMessage(HomeMarkPointSceneData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEMARKPOINTSCENEDATA._serialized_start=144
  _HOMEMARKPOINTSCENEDATA._serialized_end=332
# @@protoc_insertion_point(module_scope)
