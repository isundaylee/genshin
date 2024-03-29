# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneTeamAvatar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityControlBlock_pb2 as genshin_dot_packet_dot_proto_dot_AbilityControlBlock__pb2
from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2
from genshin.packet.proto import AvatarInfo_pb2 as genshin_dot_packet_dot_proto_dot_AvatarInfo__pb2
from genshin.packet.proto import SceneAvatarInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneAvatarInfo__pb2
from genshin.packet.proto import SceneEntityInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneEntityInfo__pb2
from genshin.packet.proto import ServerBuff_pb2 as genshin_dot_packet_dot_proto_dot_ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SceneTeamAvatar.proto\x1a.genshin/packet/proto/AbilityControlBlock.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\x1a%genshin/packet/proto/AvatarInfo.proto\x1a*genshin/packet/proto/SceneAvatarInfo.proto\x1a*genshin/packet/proto/SceneEntityInfo.proto\x1a%genshin/packet/proto/ServerBuff.proto\"\x98\x04\n\x0fSceneTeamAvatar\x12\x32\n\x13\x61vatar_ability_info\x18\x05 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12 \n\x0b\x61vatar_info\x18\x08 \x01(\x0b\x32\x0b.AvatarInfo\x12\x14\n\x0bis_on_scene\x18\x98\x01 \x01(\x08\x12\x11\n\tentity_id\x18\t \x01(\r\x12\x13\n\x0b\x61vatar_guid\x18\x0f \x01(\x04\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x12\x18\n\x10weapon_entity_id\x18\x07 \x01(\r\x12+\n\x11scene_avatar_info\x18\x03 \x01(\x0b\x32\x10.SceneAvatarInfo\x12\x13\n\x0bweapon_guid\x18\x04 \x01(\x04\x12\x32\n\x13weapon_ability_info\x18\x0b \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12+\n\x11scene_entity_info\x18\x0c \x01(\x0b\x32\x10.SceneEntityInfo\x12\x12\n\nplayer_uid\x18\x0e \x01(\r\x12\x14\n\x0cis_reconnect\x18\x06 \x01(\x08\x12\x33\n\x15\x61\x62ility_control_block\x18\x02 \x01(\x0b\x32\x14.AbilityControlBlock\x12\x1c\n\x14is_player_cur_avatar\x18\r \x01(\x08\x12%\n\x10server_buff_list\x18\n \x03(\x0b\x32\x0b.ServerBuffB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENETEAMAVATAR = DESCRIPTOR.message_types_by_name['SceneTeamAvatar']
SceneTeamAvatar = _reflection.GeneratedProtocolMessageType('SceneTeamAvatar', (_message.Message,), {
  'DESCRIPTOR' : _SCENETEAMAVATAR,
  '__module__' : 'genshin.packet.proto.SceneTeamAvatar_pb2'
  # @@protoc_insertion_point(class_scope:SceneTeamAvatar)
  })
_sym_db.RegisterMessage(SceneTeamAvatar)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENETEAMAVATAR._serialized_start=310
  _SCENETEAMAVATAR._serialized_end=846
# @@protoc_insertion_point(module_scope)
