# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HachiActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HachiStageData_pb2 as genshin_dot_packet_dot_proto_dot_HachiStageData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/HachiActivityDetailInfo.proto\x1a)genshin/packet/proto/HachiStageData.proto\"\x96\x01\n\x17HachiActivityDetailInfo\x12\x39\n\tstage_map\x18\x06 \x03(\x0b\x32&.HachiActivityDetailInfo.StageMapEntry\x1a@\n\rStageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.HachiStageData:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_HACHIACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['HachiActivityDetailInfo']
_HACHIACTIVITYDETAILINFO_STAGEMAPENTRY = _HACHIACTIVITYDETAILINFO.nested_types_by_name['StageMapEntry']
HachiActivityDetailInfo = _reflection.GeneratedProtocolMessageType('HachiActivityDetailInfo', (_message.Message,), {

  'StageMapEntry' : _reflection.GeneratedProtocolMessageType('StageMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _HACHIACTIVITYDETAILINFO_STAGEMAPENTRY,
    '__module__' : 'genshin.packet.proto.HachiActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:HachiActivityDetailInfo.StageMapEntry)
    })
  ,
  'DESCRIPTOR' : _HACHIACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.HachiActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:HachiActivityDetailInfo)
  })
_sym_db.RegisterMessage(HachiActivityDetailInfo)
_sym_db.RegisterMessage(HachiActivityDetailInfo.StageMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HACHIACTIVITYDETAILINFO_STAGEMAPENTRY._options = None
  _HACHIACTIVITYDETAILINFO_STAGEMAPENTRY._serialized_options = b'8\001'
  _HACHIACTIVITYDETAILINFO._serialized_start=98
  _HACHIACTIVITYDETAILINFO._serialized_end=248
  _HACHIACTIVITYDETAILINFO_STAGEMAPENTRY._serialized_start=184
  _HACHIACTIVITYDETAILINFO_STAGEMAPENTRY._serialized_end=248
# @@protoc_insertion_point(module_scope)
