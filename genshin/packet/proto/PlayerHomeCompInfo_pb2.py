# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerHomeCompInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendEnterHomeOption_pb2 as genshin_dot_packet_dot_proto_dot_FriendEnterHomeOption__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/PlayerHomeCompInfo.proto\x1a\x30genshin/packet/proto/FriendEnterHomeOption.proto\"\xb3\x01\n\x12PlayerHomeCompInfo\x12\x1f\n\x17unlocked_module_id_list\x18\x04 \x03(\r\x12\x1b\n\x13seen_module_id_list\x18\x02 \x03(\r\x12%\n\x1dlevelup_reward_got_level_list\x18\x07 \x03(\r\x12\x38\n\x18\x66riend_enter_home_option\x18\x08 \x01(\x0e\x32\x16.FriendEnterHomeOptionB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERHOMECOMPINFO = DESCRIPTOR.message_types_by_name['PlayerHomeCompInfo']
PlayerHomeCompInfo = _reflection.GeneratedProtocolMessageType('PlayerHomeCompInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERHOMECOMPINFO,
  '__module__' : 'genshin.packet.proto.PlayerHomeCompInfo_pb2'
  # @@protoc_insertion_point(class_scope:PlayerHomeCompInfo)
  })
_sym_db.RegisterMessage(PlayerHomeCompInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERHOMECOMPINFO._serialized_start=100
  _PLAYERHOMECOMPINFO._serialized_end=279
# @@protoc_insertion_point(module_scope)