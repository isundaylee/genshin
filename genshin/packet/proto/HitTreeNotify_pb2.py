# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/HitTreeNotify.proto
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
    'genshin/packet/proto/HitTreeNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/HitTreeNotify.proto\x1a!genshin/packet/proto/Vector.proto\"X\n\rHitTreeNotify\x12\x19\n\x08\x64rop_pos\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x19\n\x08tree_pos\x18\x03 \x01(\x0b\x32\x07.Vector\x12\x11\n\ttree_type\x18\x04 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.HitTreeNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_HITTREENOTIFY']._serialized_start=79
  _globals['_HITTREENOTIFY']._serialized_end=167
# @@protoc_insertion_point(module_scope)
