# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeVerifySceneData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeVerifyBlockData_pb2 as genshin_dot_packet_dot_proto_dot_HomeVerifyBlockData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/HomeVerifySceneData.proto\x1a.genshin/packet/proto/HomeVerifyBlockData.proto\"\x82\x01\n\x13HomeVerifySceneData\x12$\n\x06\x62locks\x18\x06 \x03(\x0b\x32\x14.HomeVerifyBlockData\x12\x11\n\tmodule_id\x18\x0b \x01(\r\x12\x10\n\x08scene_id\x18\x04 \x01(\r\x12\x0f\n\x07version\x18\x0e \x01(\r\x12\x0f\n\x07is_room\x18\x02 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEVERIFYSCENEDATA = DESCRIPTOR.message_types_by_name['HomeVerifySceneData']
HomeVerifySceneData = _reflection.GeneratedProtocolMessageType('HomeVerifySceneData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEVERIFYSCENEDATA,
  '__module__' : 'genshin.packet.proto.HomeVerifySceneData_pb2'
  # @@protoc_insertion_point(class_scope:HomeVerifySceneData)
  })
_sym_db.RegisterMessage(HomeVerifySceneData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEVERIFYSCENEDATA._serialized_start=99
  _HOMEVERIFYSCENEDATA._serialized_end=229
# @@protoc_insertion_point(module_scope)