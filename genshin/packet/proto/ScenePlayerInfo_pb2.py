# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ScenePlayerInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import OnlinePlayerInfo_pb2 as genshin_dot_packet_dot_proto_dot_OnlinePlayerInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/ScenePlayerInfo.proto\x1a+genshin/packet/proto/OnlinePlayerInfo.proto\"\x94\x01\n\x0fScenePlayerInfo\x12\x10\n\x08scene_id\x18\n \x01(\r\x12\x0f\n\x07peer_id\x18\x06 \x01(\r\x12-\n\x12online_player_info\x18\r \x01(\x0b\x32\x11.OnlinePlayerInfo\x12\x14\n\x0cis_connected\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x0f \x01(\t\x12\x0b\n\x03uid\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENEPLAYERINFO = DESCRIPTOR.message_types_by_name['ScenePlayerInfo']
ScenePlayerInfo = _reflection.GeneratedProtocolMessageType('ScenePlayerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENEPLAYERINFO,
  '__module__' : 'genshin.packet.proto.ScenePlayerInfo_pb2'
  # @@protoc_insertion_point(class_scope:ScenePlayerInfo)
  })
_sym_db.RegisterMessage(ScenePlayerInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENEPLAYERINFO._serialized_start=92
  _SCENEPLAYERINFO._serialized_end=240
# @@protoc_insertion_point(module_scope)
