# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/SceneEntityAiInfo.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'genshin/packet/proto/SceneEntityAiInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServantInfo_pb2 as genshin_dot_packet_dot_proto_dot_ServantInfo__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/SceneEntityAiInfo.proto\x1a&genshin/packet/proto/ServantInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\xea\x03\n\x11SceneEntityAiInfo\x12\x12\n\nis_ai_open\x18\x01 \x01(\x08\x12\x19\n\x08\x62orn_pos\x18\x02 \x01(\x0b\x32\x07.Vector\x12\x38\n\x0cskill_cd_map\x18\x03 \x03(\x0b\x32\".SceneEntityAiInfo.SkillCdMapEntry\x12\"\n\x0cservant_info\x18\x04 \x01(\x0b\x32\x0c.ServantInfo\x12:\n\rai_threat_map\x18\x05 \x03(\x0b\x32#.SceneEntityAiInfo.AiThreatMapEntry\x12\x43\n\x12skill_group_cd_map\x18\x06 \x03(\x0b\x32\'.SceneEntityAiInfo.SkillGroupCdMapEntry\x12\x13\n\x0b\x41JFKKOCIGHA\x18\x07 \x01(\r\x12\x13\n\x0b\x41\x41\x44JDKIFENL\x18\x08 \x01(\x08\x1a\x31\n\x0fSkillCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x32\n\x10\x41iThreatMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14SkillGroupCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.SceneEntityAiInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_SCENEENTITYAIINFO_SKILLCDMAPENTRY']._loaded_options = None
  _globals['_SCENEENTITYAIINFO_SKILLCDMAPENTRY']._serialized_options = b'8\001'
  _globals['_SCENEENTITYAIINFO_AITHREATMAPENTRY']._loaded_options = None
  _globals['_SCENEENTITYAIINFO_AITHREATMAPENTRY']._serialized_options = b'8\001'
  _globals['_SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY']._loaded_options = None
  _globals['_SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY']._serialized_options = b'8\001'
  _globals['_SCENEENTITYAIINFO']._serialized_start=124
  _globals['_SCENEENTITYAIINFO']._serialized_end=614
  _globals['_SCENEENTITYAIINFO_SKILLCDMAPENTRY']._serialized_start=457
  _globals['_SCENEENTITYAIINFO_SKILLCDMAPENTRY']._serialized_end=506
  _globals['_SCENEENTITYAIINFO_AITHREATMAPENTRY']._serialized_start=508
  _globals['_SCENEENTITYAIINFO_AITHREATMAPENTRY']._serialized_end=558
  _globals['_SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY']._serialized_start=560
  _globals['_SCENEENTITYAIINFO_SKILLGROUPCDMAPENTRY']._serialized_end=614
# @@protoc_insertion_point(module_scope)
