# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetPlayerBlacklistRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendBrief_pb2 as genshin_dot_packet_dot_proto_dot_FriendBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/GetPlayerBlacklistRsp.proto\x1a&genshin/packet/proto/FriendBrief.proto\"I\n\x15GetPlayerBlacklistRsp\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x12\x1f\n\tblacklist\x18\x03 \x03(\x0b\x32\x0c.FriendBriefB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETPLAYERBLACKLISTRSP = DESCRIPTOR.message_types_by_name['GetPlayerBlacklistRsp']
GetPlayerBlacklistRsp = _reflection.GeneratedProtocolMessageType('GetPlayerBlacklistRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETPLAYERBLACKLISTRSP,
  '__module__' : 'genshin.packet.proto.GetPlayerBlacklistRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetPlayerBlacklistRsp)
  })
_sym_db.RegisterMessage(GetPlayerBlacklistRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETPLAYERBLACKLISTRSP._serialized_start=92
  _GETPLAYERBLACKLISTRSP._serialized_end=165
# @@protoc_insertion_point(module_scope)