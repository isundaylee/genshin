# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarEnterSceneInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2
from genshin.packet.proto import ServerBuff_pb2 as genshin_dot_packet_dot_proto_dot_ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/AvatarEnterSceneInfo.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\x1a%genshin/packet/proto/ServerBuff.proto\"\x99\x02\n\x14\x41vatarEnterSceneInfo\x12%\n\x10server_buff_list\x18\x0e \x03(\x0b\x32\x0b.ServerBuff\x12\x18\n\x10\x61vatar_entity_id\x18\x07 \x01(\r\x12\x32\n\x13weapon_ability_info\x18\x0c \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x18\n\x10weapon_entity_id\x18\n \x01(\r\x12\x32\n\x13\x61vatar_ability_info\x18\x02 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x13\n\x0b\x61vatar_guid\x18\r \x01(\x04\x12\x13\n\x0bweapon_guid\x18\t \x01(\x04\x12\x14\n\x0c\x62uff_id_list\x18\x05 \x03(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AVATARENTERSCENEINFO = DESCRIPTOR.message_types_by_name['AvatarEnterSceneInfo']
AvatarEnterSceneInfo = _reflection.GeneratedProtocolMessageType('AvatarEnterSceneInfo', (_message.Message,), {
  'DESCRIPTOR' : _AVATARENTERSCENEINFO,
  '__module__' : 'genshin.packet.proto.AvatarEnterSceneInfo_pb2'
  # @@protoc_insertion_point(class_scope:AvatarEnterSceneInfo)
  })
_sym_db.RegisterMessage(AvatarEnterSceneInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AVATARENTERSCENEINFO._serialized_start=140
  _AVATARENTERSCENEINFO._serialized_end=421
# @@protoc_insertion_point(module_scope)
