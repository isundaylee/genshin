# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetPlayerAskFriendListRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendBrief_pb2 as genshin_dot_packet_dot_proto_dot_FriendBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/GetPlayerAskFriendListRsp.proto\x1a&genshin/packet/proto/FriendBrief.proto\"S\n\x19GetPlayerAskFriendListRsp\x12\x0f\n\x07retcode\x18\r \x01(\x05\x12%\n\x0f\x61sk_friend_list\x18\x0f \x03(\x0b\x32\x0c.FriendBriefB\x16\n\x14org.sorapointa.protob\x06proto3')



_GETPLAYERASKFRIENDLISTRSP = DESCRIPTOR.message_types_by_name['GetPlayerAskFriendListRsp']
GetPlayerAskFriendListRsp = _reflection.GeneratedProtocolMessageType('GetPlayerAskFriendListRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETPLAYERASKFRIENDLISTRSP,
  '__module__' : 'genshin.packet.proto.GetPlayerAskFriendListRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetPlayerAskFriendListRsp)
  })
_sym_db.RegisterMessage(GetPlayerAskFriendListRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETPLAYERASKFRIENDLISTRSP._serialized_start=96
  _GETPLAYERASKFRIENDLISTRSP._serialized_end=179
# @@protoc_insertion_point(module_scope)
