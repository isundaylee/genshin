# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AddBlacklistRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendBrief_pb2 as genshin_dot_packet_dot_proto_dot_FriendBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/AddBlacklistRsp.proto\x1a&genshin/packet/proto/FriendBrief.proto\"M\n\x0f\x41\x64\x64\x42lacklistRsp\x12)\n\x13target_friend_brief\x18\r \x01(\x0b\x32\x0c.FriendBrief\x12\x0f\n\x07retcode\x18\x07 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_ADDBLACKLISTRSP = DESCRIPTOR.message_types_by_name['AddBlacklistRsp']
AddBlacklistRsp = _reflection.GeneratedProtocolMessageType('AddBlacklistRsp', (_message.Message,), {
  'DESCRIPTOR' : _ADDBLACKLISTRSP,
  '__module__' : 'genshin.packet.proto.AddBlacklistRsp_pb2'
  # @@protoc_insertion_point(class_scope:AddBlacklistRsp)
  })
_sym_db.RegisterMessage(AddBlacklistRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ADDBLACKLISTRSP._serialized_start=86
  _ADDBLACKLISTRSP._serialized_end=163
# @@protoc_insertion_point(module_scope)
