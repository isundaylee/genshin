# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ScenePlayerLocationNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlayerLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlayerLocationInfo__pb2
from genshin.packet.proto import VehicleLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_VehicleLocationInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/ScenePlayerLocationNotify.proto\x1a-genshin/packet/proto/PlayerLocationInfo.proto\x1a.genshin/packet/proto/VehicleLocationInfo.proto\"\x8b\x01\n\x19ScenePlayerLocationNotify\x12.\n\x10vehicle_loc_list\x18\x03 \x03(\x0b\x32\x14.VehicleLocationInfo\x12\x10\n\x08scene_id\x18\t \x01(\r\x12,\n\x0fplayer_loc_list\x18\x0e \x03(\x0b\x32\x13.PlayerLocationInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SCENEPLAYERLOCATIONNOTIFY = DESCRIPTOR.message_types_by_name['ScenePlayerLocationNotify']
ScenePlayerLocationNotify = _reflection.GeneratedProtocolMessageType('ScenePlayerLocationNotify', (_message.Message,), {
  'DESCRIPTOR' : _SCENEPLAYERLOCATIONNOTIFY,
  '__module__' : 'genshin.packet.proto.ScenePlayerLocationNotify_pb2'
  # @@protoc_insertion_point(class_scope:ScenePlayerLocationNotify)
  })
_sym_db.RegisterMessage(ScenePlayerLocationNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SCENEPLAYERLOCATIONNOTIFY._serialized_start=152
  _SCENEPLAYERLOCATIONNOTIFY._serialized_end=291
# @@protoc_insertion_point(module_scope)