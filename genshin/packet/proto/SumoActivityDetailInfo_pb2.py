# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SumoActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SumoStageData_pb2 as genshin_dot_packet_dot_proto_dot_SumoStageData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/SumoActivityDetailInfo.proto\x1a(genshin/packet/proto/SumoStageData.proto\"\xd4\x01\n\x16SumoActivityDetailInfo\x12\x15\n\rdifficulty_id\x18\x0b \x01(\r\x12\x41\n\x0esumo_stage_map\x18\r \x03(\x0b\x32).SumoActivityDetailInfo.SumoStageMapEntry\x12\x1b\n\x13Unk2700_NIJIAJMFLLD\x18\x0e \x01(\r\x1a\x43\n\x11SumoStageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.SumoStageData:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SUMOACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['SumoActivityDetailInfo']
_SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY = _SUMOACTIVITYDETAILINFO.nested_types_by_name['SumoStageMapEntry']
SumoActivityDetailInfo = _reflection.GeneratedProtocolMessageType('SumoActivityDetailInfo', (_message.Message,), {

  'SumoStageMapEntry' : _reflection.GeneratedProtocolMessageType('SumoStageMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY,
    '__module__' : 'genshin.packet.proto.SumoActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:SumoActivityDetailInfo.SumoStageMapEntry)
    })
  ,
  'DESCRIPTOR' : _SUMOACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.SumoActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:SumoActivityDetailInfo)
  })
_sym_db.RegisterMessage(SumoActivityDetailInfo)
_sym_db.RegisterMessage(SumoActivityDetailInfo.SumoStageMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY._options = None
  _SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY._serialized_options = b'8\001'
  _SUMOACTIVITYDETAILINFO._serialized_start=96
  _SUMOACTIVITYDETAILINFO._serialized_end=308
  _SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY._serialized_start=241
  _SUMOACTIVITYDETAILINFO_SUMOSTAGEMAPENTRY._serialized_end=308
# @@protoc_insertion_point(module_scope)
