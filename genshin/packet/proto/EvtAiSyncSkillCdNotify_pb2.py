# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EvtAiSyncSkillCdNotify.proto
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
    'genshin/packet/proto/EvtAiSyncSkillCdNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AiSkillCdInfo_pb2 as genshin_dot_packet_dot_proto_dot_AiSkillCdInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/EvtAiSyncSkillCdNotify.proto\x1a(genshin/packet/proto/AiSkillCdInfo.proto\"\x91\x01\n\x16\x45vtAiSyncSkillCdNotify\x12\x37\n\tai_cd_map\x18\x0b \x03(\x0b\x32$.EvtAiSyncSkillCdNotify.AiCdMapEntry\x1a>\n\x0c\x41iCdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.AiSkillCdInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EvtAiSyncSkillCdNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_EVTAISYNCSKILLCDNOTIFY_AICDMAPENTRY']._loaded_options = None
  _globals['_EVTAISYNCSKILLCDNOTIFY_AICDMAPENTRY']._serialized_options = b'8\001'
  _globals['_EVTAISYNCSKILLCDNOTIFY']._serialized_start=96
  _globals['_EVTAISYNCSKILLCDNOTIFY']._serialized_end=241
  _globals['_EVTAISYNCSKILLCDNOTIFY_AICDMAPENTRY']._serialized_start=179
  _globals['_EVTAISYNCSKILLCDNOTIFY_AICDMAPENTRY']._serialized_end=241
# @@protoc_insertion_point(module_scope)
