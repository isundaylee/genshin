# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/DungeonChallengeBeginNotify.proto
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
    'genshin/packet/proto/DungeonChallengeBeginNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/DungeonChallengeBeginNotify.proto\"\x9a\x01\n\x1b\x44ungeonChallengeBeginNotify\x12\x12\n\nparam_list\x18\x03 \x03(\r\x12\x17\n\x0f\x63hallenge_index\x18\x05 \x01(\r\x12\x14\n\x0c\x66\x61ther_index\x18\x07 \x01(\r\x12\x10\n\x08uid_list\x18\x08 \x03(\r\x12\x14\n\x0c\x63hallenge_id\x18\t \x01(\r\x12\x10\n\x08group_id\x18\n \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.DungeonChallengeBeginNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_DUNGEONCHALLENGEBEGINNOTIFY']._serialized_start=59
  _globals['_DUNGEONCHALLENGEBEGINNOTIFY']._serialized_end=213
# @@protoc_insertion_point(module_scope)
