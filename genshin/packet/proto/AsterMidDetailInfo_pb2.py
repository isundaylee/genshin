# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AsterMidDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AsterMidCampInfo_pb2 as genshin_dot_packet_dot_proto_dot_AsterMidCampInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/AsterMidDetailInfo.proto\x1a+genshin/packet/proto/AsterMidCampInfo.proto\"v\n\x12\x41sterMidDetailInfo\x12\x12\n\nbegin_time\x18\n \x01(\r\x12$\n\tcamp_list\x18\x07 \x03(\x0b\x32\x11.AsterMidCampInfo\x12\x0f\n\x07is_open\x18\x04 \x01(\x08\x12\x15\n\rcollect_count\x18\x0b \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_ASTERMIDDETAILINFO = DESCRIPTOR.message_types_by_name['AsterMidDetailInfo']
AsterMidDetailInfo = _reflection.GeneratedProtocolMessageType('AsterMidDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _ASTERMIDDETAILINFO,
  '__module__' : 'genshin.packet.proto.AsterMidDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:AsterMidDetailInfo)
  })
_sym_db.RegisterMessage(AsterMidDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ASTERMIDDETAILINFO._serialized_start=94
  _ASTERMIDDETAILINFO._serialized_end=212
# @@protoc_insertion_point(module_scope)
