# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/BreakoutSpawnPoint.proto
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
    'genshin/packet/proto/BreakoutSpawnPoint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BreakoutPhysicalObject_pb2 as genshin_dot_packet_dot_proto_dot_BreakoutPhysicalObject__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/BreakoutSpawnPoint.proto\x1a\x31genshin/packet/proto/BreakoutPhysicalObject.proto\"m\n\x12\x42reakoutSpawnPoint\x12\n\n\x02id\x18\x01 \x01(\r\x12\x16\n\x0e\x62rick_suite_id\x18\x02 \x01(\r\x12\x33\n\x12spawned_brick_list\x18\x03 \x03(\x0b\x32\x17.BreakoutPhysicalObjectB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.BreakoutSpawnPoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BREAKOUTSPAWNPOINT']._serialized_start=100
  _globals['_BREAKOUTSPAWNPOINT']._serialized_end=209
# @@protoc_insertion_point(module_scope)
