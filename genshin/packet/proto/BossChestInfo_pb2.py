# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/BossChestInfo.proto
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
    'genshin/packet/proto/BossChestInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WeeklyBossResinDiscountInfo_pb2 as genshin_dot_packet_dot_proto_dot_WeeklyBossResinDiscountInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/BossChestInfo.proto\x1a\x36genshin/packet/proto/WeeklyBossResinDiscountInfo.proto\"\xff\x01\n\rBossChestInfo\x12\x19\n\x11monster_config_id\x18\x01 \x01(\r\x12\r\n\x05resin\x18\x02 \x01(\r\x12\x17\n\x0fremain_uid_list\x18\x03 \x03(\r\x12\x18\n\x10qualify_uid_list\x18\x04 \x03(\r\x12<\n\x10uid_discount_map\x18\x05 \x03(\x0b\x32\".BossChestInfo.UidDiscountMapEntry\x1aS\n\x13UidDiscountMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.WeeklyBossResinDiscountInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.BossChestInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BOSSCHESTINFO_UIDDISCOUNTMAPENTRY']._loaded_options = None
  _globals['_BOSSCHESTINFO_UIDDISCOUNTMAPENTRY']._serialized_options = b'8\001'
  _globals['_BOSSCHESTINFO']._serialized_start=101
  _globals['_BOSSCHESTINFO']._serialized_end=356
  _globals['_BOSSCHESTINFO_UIDDISCOUNTMAPENTRY']._serialized_start=273
  _globals['_BOSSCHESTINFO_UIDDISCOUNTMAPENTRY']._serialized_end=356
# @@protoc_insertion_point(module_scope)
