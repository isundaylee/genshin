# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EffigyActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EffigyDailyInfo_pb2 as genshin_dot_packet_dot_proto_dot_EffigyDailyInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/EffigyActivityDetailInfo.proto\x1a*genshin/packet/proto/EffigyDailyInfo.proto\"\x95\x01\n\x18\x45\x66\x66igyActivityDetailInfo\x12\x11\n\tcur_score\x18\x05 \x01(\r\x12)\n\x0f\x64\x61ily_info_list\x18\x0e \x03(\x0b\x32\x10.EffigyDailyInfo\x12\x1a\n\x12last_difficulty_id\x18\t \x01(\r\x12\x1f\n\x17taken_reward_index_list\x18\x02 \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_EFFIGYACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['EffigyActivityDetailInfo']
EffigyActivityDetailInfo = _reflection.GeneratedProtocolMessageType('EffigyActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _EFFIGYACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.EffigyActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:EffigyActivityDetailInfo)
  })
_sym_db.RegisterMessage(EffigyActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EFFIGYACTIVITYDETAILINFO._serialized_start=100
  _EFFIGYACTIVITYDETAILINFO._serialized_end=249
# @@protoc_insertion_point(module_scope)