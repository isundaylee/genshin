# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/TeamEnterSceneInfo.proto
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
    'genshin/packet/proto/TeamEnterSceneInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2
from genshin.packet.proto import AbilityControlBlock_pb2 as genshin_dot_packet_dot_proto_dot_AbilityControlBlock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/TeamEnterSceneInfo.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\x1a.genshin/packet/proto/AbilityControlBlock.proto\"\x93\x01\n\x12TeamEnterSceneInfo\x12\x16\n\x0eteam_entity_id\x18\x01 \x01(\r\x12\x30\n\x11team_ability_info\x18\x05 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x33\n\x15\x61\x62ility_control_block\x18\x0f \x01(\x0b\x32\x14.AbilityControlBlockB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.TeamEnterSceneInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_TEAMENTERSCENEINFO']._serialized_start=147
  _globals['_TEAMENTERSCENEINFO']._serialized_end=294
# @@protoc_insertion_point(module_scope)
