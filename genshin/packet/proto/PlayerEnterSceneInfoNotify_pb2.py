# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerEnterSceneInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AvatarEnterSceneInfo_pb2 as genshin_dot_packet_dot_proto_dot_AvatarEnterSceneInfo__pb2
from genshin.packet.proto import MPLevelEntityInfo_pb2 as genshin_dot_packet_dot_proto_dot_MPLevelEntityInfo__pb2
from genshin.packet.proto import TeamEnterSceneInfo_pb2 as genshin_dot_packet_dot_proto_dot_TeamEnterSceneInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/PlayerEnterSceneInfoNotify.proto\x1a/genshin/packet/proto/AvatarEnterSceneInfo.proto\x1a,genshin/packet/proto/MPLevelEntityInfo.proto\x1a-genshin/packet/proto/TeamEnterSceneInfo.proto\"\xe7\x01\n\x1aPlayerEnterSceneInfoNotify\x12,\n\x0fteam_enter_info\x18\x08 \x01(\x0b\x32\x13.TeamEnterSceneInfo\x12\x19\n\x11\x65nter_scene_token\x18\x0c \x01(\r\x12\x30\n\x11\x61vatar_enter_info\x18\x07 \x03(\x0b\x32\x15.AvatarEnterSceneInfo\x12\x1c\n\x14\x63ur_avatar_entity_id\x18\x06 \x01(\r\x12\x30\n\x14mp_level_entity_info\x18\x05 \x01(\x0b\x32\x12.MPLevelEntityInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERENTERSCENEINFONOTIFY = DESCRIPTOR.message_types_by_name['PlayerEnterSceneInfoNotify']
PlayerEnterSceneInfoNotify = _reflection.GeneratedProtocolMessageType('PlayerEnterSceneInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERENTERSCENEINFONOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerEnterSceneInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerEnterSceneInfoNotify)
  })
_sym_db.RegisterMessage(PlayerEnterSceneInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERENTERSCENEINFONOTIFY._serialized_start=200
  _PLAYERENTERSCENEINFONOTIFY._serialized_end=431
# @@protoc_insertion_point(module_scope)
