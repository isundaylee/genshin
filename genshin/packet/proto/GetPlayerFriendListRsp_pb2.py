# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetPlayerFriendListRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendBrief_pb2 as genshin_dot_packet_dot_proto_dot_FriendBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/GetPlayerFriendListRsp.proto\x1a&genshin/packet/proto/FriendBrief.proto\"s\n\x16GetPlayerFriendListRsp\x12\x0f\n\x07retcode\x18\t \x01(\x05\x12%\n\x0f\x61sk_friend_list\x18\x08 \x03(\x0b\x32\x0c.FriendBrief\x12!\n\x0b\x66riend_list\x18\x0e \x03(\x0b\x32\x0c.FriendBriefB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETPLAYERFRIENDLISTRSP = DESCRIPTOR.message_types_by_name['GetPlayerFriendListRsp']
GetPlayerFriendListRsp = _reflection.GeneratedProtocolMessageType('GetPlayerFriendListRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETPLAYERFRIENDLISTRSP,
  '__module__' : 'genshin.packet.proto.GetPlayerFriendListRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetPlayerFriendListRsp)
  })
_sym_db.RegisterMessage(GetPlayerFriendListRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETPLAYERFRIENDLISTRSP._serialized_start=93
  _GETPLAYERFRIENDLISTRSP._serialized_end=208
# @@protoc_insertion_point(module_scope)
