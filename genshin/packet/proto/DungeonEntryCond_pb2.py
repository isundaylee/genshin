# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/DungeonEntryCond.proto
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
    'genshin/packet/proto/DungeonEntryCond.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DungeonEntryBlockReason_pb2 as genshin_dot_packet_dot_proto_dot_DungeonEntryBlockReason__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/DungeonEntryCond.proto\x1a\x32genshin/packet/proto/DungeonEntryBlockReason.proto\"Q\n\x10\x44ungeonEntryCond\x12-\n\x0b\x63ond_reason\x18\x0f \x01(\x0e\x32\x18.DungeonEntryBlockReason\x12\x0e\n\x06param1\x18\r \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.DungeonEntryCond_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_DUNGEONENTRYCOND']._serialized_start=99
  _globals['_DUNGEONENTRYCOND']._serialized_end=180
# @@protoc_insertion_point(module_scope)
