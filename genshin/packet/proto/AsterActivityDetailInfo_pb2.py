# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AsterActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AsterLargeDetailInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterLargeDetailInfo__pb2
from genshin.packet.proto import AsterLittleDetailInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterLittleDetailInfo__pb2
from genshin.packet.proto import AsterMidDetailInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterMidDetailInfo__pb2
from genshin.packet.proto import AsterProgressDetailInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterProgressDetailInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/AsterActivityDetailInfo.proto\x1a/genshin/packet/proto/AsterLargeDetailInfo.proto\x1a\x30genshin/packet/proto/AsterLittleDetailInfo.proto\x1a-genshin/packet/proto/AsterMidDetailInfo.proto\x1a\x32genshin/packet/proto/AsterProgressDetailInfo.proto\"\xd0\x02\n\x17\x41sterActivityDetailInfo\x12,\n\x0c\x61ster_little\x18\x07 \x01(\x0b\x32\x16.AsterLittleDetailInfo\x12\x14\n\x0c\x61ster_credit\x18\x0e \x01(\r\x12*\n\x0b\x61ster_large\x18\t \x01(\x0b\x32\x15.AsterLargeDetailInfo\x12\x1f\n\x17is_special_reward_taken\x18\x01 \x01(\x08\x12\x19\n\x11is_content_closed\x18\r \x01(\x08\x12\x1a\n\x12\x63ontent_close_time\x18\x08 \x01(\r\x12\x13\n\x0b\x61ster_token\x18\x05 \x01(\r\x12&\n\taster_mid\x18\x06 \x01(\x0b\x32\x13.AsterMidDetailInfo\x12\x30\n\x0e\x61ster_progress\x18\x02 \x01(\x0b\x32\x18.AsterProgressDetailInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_ASTERACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['AsterActivityDetailInfo']
AsterActivityDetailInfo = _reflection.GeneratedProtocolMessageType('AsterActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _ASTERACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.AsterActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:AsterActivityDetailInfo)
  })
_sym_db.RegisterMessage(AsterActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ASTERACTIVITYDETAILINFO._serialized_start=253
  _ASTERACTIVITYDETAILINFO._serialized_end=589
# @@protoc_insertion_point(module_scope)