# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HideAndSeekStageInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HideAndSeekPlayerBattleInfo_pb2 as genshin_dot_packet_dot_proto_dot_HideAndSeekPlayerBattleInfo__pb2
from genshin.packet.proto import HideAndSeekStageType_pb2 as genshin_dot_packet_dot_proto_dot_HideAndSeekStageType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/HideAndSeekStageInfo.proto\x1a\x36genshin/packet/proto/HideAndSeekPlayerBattleInfo.proto\x1a/genshin/packet/proto/HideAndSeekStageType.proto\"\xad\x02\n\x14HideAndSeekStageInfo\x12\x0e\n\x06map_id\x18\x08 \x01(\r\x12\x17\n\x0fis_record_score\x18\x03 \x01(\x08\x12)\n\nstage_type\x18\x07 \x01(\x0e\x32\x15.HideAndSeekStageType\x12\x41\n\x0f\x62\x61ttle_info_map\x18\x02 \x03(\x0b\x32(.HideAndSeekStageInfo.BattleInfoMapEntry\x12\x16\n\x0ehider_uid_list\x18\x01 \x03(\r\x12\x12\n\nhunter_uid\x18\n \x01(\r\x1aR\n\x12\x42\x61ttleInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.HideAndSeekPlayerBattleInfo:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_HIDEANDSEEKSTAGEINFO = DESCRIPTOR.message_types_by_name['HideAndSeekStageInfo']
_HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY = _HIDEANDSEEKSTAGEINFO.nested_types_by_name['BattleInfoMapEntry']
HideAndSeekStageInfo = _reflection.GeneratedProtocolMessageType('HideAndSeekStageInfo', (_message.Message,), {

  'BattleInfoMapEntry' : _reflection.GeneratedProtocolMessageType('BattleInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.HideAndSeekStageInfo_pb2'
    # @@protoc_insertion_point(class_scope:HideAndSeekStageInfo.BattleInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _HIDEANDSEEKSTAGEINFO,
  '__module__' : 'genshin.packet.proto.HideAndSeekStageInfo_pb2'
  # @@protoc_insertion_point(class_scope:HideAndSeekStageInfo)
  })
_sym_db.RegisterMessage(HideAndSeekStageInfo)
_sym_db.RegisterMessage(HideAndSeekStageInfo.BattleInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._options = None
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_options = b'8\001'
  _HIDEANDSEEKSTAGEINFO._serialized_start=157
  _HIDEANDSEEKSTAGEINFO._serialized_end=458
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_start=376
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_end=458
# @@protoc_insertion_point(module_scope)