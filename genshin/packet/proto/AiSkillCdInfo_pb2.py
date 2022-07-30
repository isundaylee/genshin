# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AiSkillCdInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/AiSkillCdInfo.proto\"\xf1\x01\n\rAiSkillCdInfo\x12\x34\n\x0cskill_cd_map\x18\x0b \x03(\x0b\x32\x1e.AiSkillCdInfo.SkillCdMapEntry\x12?\n\x12skill_group_cd_map\x18\x06 \x03(\x0b\x32#.AiSkillCdInfo.SkillGroupCdMapEntry\x1a\x31\n\x0fSkillCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14SkillGroupCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AISKILLCDINFO = DESCRIPTOR.message_types_by_name['AiSkillCdInfo']
_AISKILLCDINFO_SKILLCDMAPENTRY = _AISKILLCDINFO.nested_types_by_name['SkillCdMapEntry']
_AISKILLCDINFO_SKILLGROUPCDMAPENTRY = _AISKILLCDINFO.nested_types_by_name['SkillGroupCdMapEntry']
AiSkillCdInfo = _reflection.GeneratedProtocolMessageType('AiSkillCdInfo', (_message.Message,), {

  'SkillCdMapEntry' : _reflection.GeneratedProtocolMessageType('SkillCdMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AISKILLCDINFO_SKILLCDMAPENTRY,
    '__module__' : 'genshin.packet.proto.AiSkillCdInfo_pb2'
    # @@protoc_insertion_point(class_scope:AiSkillCdInfo.SkillCdMapEntry)
    })
  ,

  'SkillGroupCdMapEntry' : _reflection.GeneratedProtocolMessageType('SkillGroupCdMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AISKILLCDINFO_SKILLGROUPCDMAPENTRY,
    '__module__' : 'genshin.packet.proto.AiSkillCdInfo_pb2'
    # @@protoc_insertion_point(class_scope:AiSkillCdInfo.SkillGroupCdMapEntry)
    })
  ,
  'DESCRIPTOR' : _AISKILLCDINFO,
  '__module__' : 'genshin.packet.proto.AiSkillCdInfo_pb2'
  # @@protoc_insertion_point(class_scope:AiSkillCdInfo)
  })
_sym_db.RegisterMessage(AiSkillCdInfo)
_sym_db.RegisterMessage(AiSkillCdInfo.SkillCdMapEntry)
_sym_db.RegisterMessage(AiSkillCdInfo.SkillGroupCdMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AISKILLCDINFO_SKILLCDMAPENTRY._options = None
  _AISKILLCDINFO_SKILLCDMAPENTRY._serialized_options = b'8\001'
  _AISKILLCDINFO_SKILLGROUPCDMAPENTRY._options = None
  _AISKILLCDINFO_SKILLGROUPCDMAPENTRY._serialized_options = b'8\001'
  _AISKILLCDINFO._serialized_start=45
  _AISKILLCDINFO._serialized_end=286
  _AISKILLCDINFO_SKILLCDMAPENTRY._serialized_start=181
  _AISKILLCDINFO_SKILLCDMAPENTRY._serialized_end=230
  _AISKILLCDINFO_SKILLGROUPCDMAPENTRY._serialized_start=232
  _AISKILLCDINFO_SKILLGROUPCDMAPENTRY._serialized_end=286
# @@protoc_insertion_point(module_scope)