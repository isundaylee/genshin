# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneEntityAiInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServantInfo_pb2 as genshin_dot_packet_dot_proto_dot_ServantInfo__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/SceneEntityAiInfo.proto\x1a&genshin/packet/proto/ServantInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\xd4\x03\n\x11SceneEntityAiInfo\x12\x12\n\nis_ai_open\x18\x01 \x01(\x08\x12\x19\n\x08\x62orn_pos\x18\x02 \x01(\x0b\x32\x07.Vector\x12\x38\n\x0cskill_cd_map\x18\x03 \x03(\x0b\x32\".SceneEntityAiInfo.SkillCdMapEntry\x12\"\n\x0cservant_info\x18\x04 \x01(\x0b\x32\x0c.ServantInfo\x12:\n\rai_threat_map\x18\x05 \x03(\x0b\x32#.SceneEntityAiInfo.AiThreatMapEntry\x12\x43\n\x12skill_group_cd_map\x18\x06 \x03(\x0b\x32\'.SceneEntityAiInfo.SkillGroupCdMapEntry\x12\x12\n\ncur_tactic\x18\x07 \x01(\r\x1a\x31\n\x0fSkillCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x32\n\x10\x41iThreatMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14SkillGroupCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SCENEENTITYAIINFO = DESCRIPTOR.message_types_by_name['SceneEntityAiInfo']
_SCENEENTITYAIINFO_SKILLCDMAPENTRY = _SCENEENTITYAIINFO.nested_types_by_name['SkillCdMapEntry']
_SCENEENTITYAIINFO_AITHREATMAPENTRY = _SCENEENTITYAIINFO.nested_types_by_name['AiThreatMapEntry']
_SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY = _SCENEENTITYAIINFO.nested_types_by_name['SkillGroupCdMapEntry']
SceneEntityAiInfo = _reflection.GeneratedProtocolMessageType('SceneEntityAiInfo', (_message.Message,), {

  'SkillCdMapEntry' : _reflection.GeneratedProtocolMessageType('SkillCdMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCENEENTITYAIINFO_SKILLCDMAPENTRY,
    '__module__' : 'genshin.packet.proto.SceneEntityAiInfo_pb2'
    # @@protoc_insertion_point(class_scope:SceneEntityAiInfo.SkillCdMapEntry)
    })
  ,

  'AiThreatMapEntry' : _reflection.GeneratedProtocolMessageType('AiThreatMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCENEENTITYAIINFO_AITHREATMAPENTRY,
    '__module__' : 'genshin.packet.proto.SceneEntityAiInfo_pb2'
    # @@protoc_insertion_point(class_scope:SceneEntityAiInfo.AiThreatMapEntry)
    })
  ,

  'SkillGroupCdMapEntry' : _reflection.GeneratedProtocolMessageType('SkillGroupCdMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY,
    '__module__' : 'genshin.packet.proto.SceneEntityAiInfo_pb2'
    # @@protoc_insertion_point(class_scope:SceneEntityAiInfo.SkillGroupCdMapEntry)
    })
  ,
  'DESCRIPTOR' : _SCENEENTITYAIINFO,
  '__module__' : 'genshin.packet.proto.SceneEntityAiInfo_pb2'
  # @@protoc_insertion_point(class_scope:SceneEntityAiInfo)
  })
_sym_db.RegisterMessage(SceneEntityAiInfo)
_sym_db.RegisterMessage(SceneEntityAiInfo.SkillCdMapEntry)
_sym_db.RegisterMessage(SceneEntityAiInfo.AiThreatMapEntry)
_sym_db.RegisterMessage(SceneEntityAiInfo.SkillGroupCdMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SCENEENTITYAIINFO_SKILLCDMAPENTRY._options = None
  _SCENEENTITYAIINFO_SKILLCDMAPENTRY._serialized_options = b'8\001'
  _SCENEENTITYAIINFO_AITHREATMAPENTRY._options = None
  _SCENEENTITYAIINFO_AITHREATMAPENTRY._serialized_options = b'8\001'
  _SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY._options = None
  _SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY._serialized_options = b'8\001'
  _SCENEENTITYAIINFO._serialized_start=124
  _SCENEENTITYAIINFO._serialized_end=592
  _SCENEENTITYAIINFO_SKILLCDMAPENTRY._serialized_start=435
  _SCENEENTITYAIINFO_SKILLCDMAPENTRY._serialized_end=484
  _SCENEENTITYAIINFO_AITHREATMAPENTRY._serialized_start=486
  _SCENEENTITYAIINFO_AITHREATMAPENTRY._serialized_end=536
  _SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY._serialized_start=538
  _SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY._serialized_end=592
# @@protoc_insertion_point(module_scope)
