# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CrucibleActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CrucibleBattleUidInfo_pb2 as genshin_dot_packet_dot_proto_dot_CrucibleBattleUidInfo__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/CrucibleActivityDetailInfo.proto\x1a\x30genshin/packet/proto/CrucibleBattleUidInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\x90\x01\n\x1a\x43rucibleActivityDetailInfo\x12\x11\n\tcost_time\x18\x05 \x01(\r\x12\x1a\n\x12\x62\x61ttle_world_level\x18\x0c \x01(\r\x12-\n\ruid_info_list\x18\x03 \x03(\x0b\x32\x16.CrucibleBattleUidInfo\x12\x14\n\x03pos\x18\t \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_CRUCIBLEACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['CrucibleActivityDetailInfo']
CrucibleActivityDetailInfo = _reflection.GeneratedProtocolMessageType('CrucibleActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _CRUCIBLEACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.CrucibleActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:CrucibleActivityDetailInfo)
  })
_sym_db.RegisterMessage(CrucibleActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CRUCIBLEACTIVITYDETAILINFO._serialized_start=143
  _CRUCIBLEACTIVITYDETAILINFO._serialized_end=287
# @@protoc_insertion_point(module_scope)