# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeAvatarTalkRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeAvatarTalkFinishInfo_pb2 as genshin_dot_packet_dot_proto_dot_HomeAvatarTalkFinishInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/HomeAvatarTalkRsp.proto\x1a\x33genshin/packet/proto/HomeAvatarTalkFinishInfo.proto\"Y\n\x11HomeAvatarTalkRsp\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x12\x33\n\x10\x61vatar_talk_info\x18\x03 \x01(\x0b\x32\x19.HomeAvatarTalkFinishInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEAVATARTALKRSP = DESCRIPTOR.message_types_by_name['HomeAvatarTalkRsp']
HomeAvatarTalkRsp = _reflection.GeneratedProtocolMessageType('HomeAvatarTalkRsp', (_message.Message,), {
  'DESCRIPTOR' : _HOMEAVATARTALKRSP,
  '__module__' : 'genshin.packet.proto.HomeAvatarTalkRsp_pb2'
  # @@protoc_insertion_point(class_scope:HomeAvatarTalkRsp)
  })
_sym_db.RegisterMessage(HomeAvatarTalkRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEAVATARTALKRSP._serialized_start=101
  _HOMEAVATARTALKRSP._serialized_end=190
# @@protoc_insertion_point(module_scope)
