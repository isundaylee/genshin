# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetBonusActivityRewardRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BonusActivityInfo_pb2 as genshin_dot_packet_dot_proto_dot_BonusActivityInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/GetBonusActivityRewardRsp.proto\x1a,genshin/packet/proto/BonusActivityInfo.proto\"b\n\x19GetBonusActivityRewardRsp\x12\x34\n\x18\x62onus_activity_info_list\x18\x04 \x01(\x0b\x32\x12.BonusActivityInfo\x12\x0f\n\x07retcode\x18\r \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GETBONUSACTIVITYREWARDRSP = DESCRIPTOR.message_types_by_name['GetBonusActivityRewardRsp']
GetBonusActivityRewardRsp = _reflection.GeneratedProtocolMessageType('GetBonusActivityRewardRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETBONUSACTIVITYREWARDRSP,
  '__module__' : 'genshin.packet.proto.GetBonusActivityRewardRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetBonusActivityRewardRsp)
  })
_sym_db.RegisterMessage(GetBonusActivityRewardRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETBONUSACTIVITYREWARDRSP._serialized_start=102
  _GETBONUSACTIVITYREWARDRSP._serialized_end=200
# @@protoc_insertion_point(module_scope)
