# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TrialAvatarActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import TrialAvatarActivityRewardDetailInfo_pb2 as genshin_dot_packet_dot_proto_dot_TrialAvatarActivityRewardDetailInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/TrialAvatarActivityDetailInfo.proto\x1a>genshin/packet/proto/TrialAvatarActivityRewardDetailInfo.proto\"_\n\x1dTrialAvatarActivityDetailInfo\x12>\n\x10reward_info_list\x18\r \x03(\x0b\x32$.TrialAvatarActivityRewardDetailInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_TRIALAVATARACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['TrialAvatarActivityDetailInfo']
TrialAvatarActivityDetailInfo = _reflection.GeneratedProtocolMessageType('TrialAvatarActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRIALAVATARACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.TrialAvatarActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:TrialAvatarActivityDetailInfo)
  })
_sym_db.RegisterMessage(TrialAvatarActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TRIALAVATARACTIVITYDETAILINFO._serialized_start=124
  _TRIALAVATARACTIVITYDETAILINFO._serialized_end=219
# @@protoc_insertion_point(module_scope)