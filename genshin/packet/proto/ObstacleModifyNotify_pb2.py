# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ObstacleModifyNotify.proto
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
    'genshin/packet/proto/ObstacleModifyNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ObstacleInfo_pb2 as genshin_dot_packet_dot_proto_dot_ObstacleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/ObstacleModifyNotify.proto\x1a\'genshin/packet/proto/ObstacleInfo.proto\"\x95\x01\n\x14ObstacleModifyNotify\x12$\n\radd_obstacles\x18\x02 \x03(\x0b\x32\r.ObstacleInfo\x12\x13\n\x0bPBGEEKLDIKE\x18\x05 \x03(\x05\x12\x1b\n\x13remove_obstacle_ids\x18\t \x03(\x05\x12\x13\n\x0b\x45HFGKOLBOMK\x18\x0c \x03(\x05\x12\x10\n\x08scene_id\x18\x0e \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ObstacleModifyNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_OBSTACLEMODIFYNOTIFY']._serialized_start=93
  _globals['_OBSTACLEMODIFYNOTIFY']._serialized_end=242
# @@protoc_insertion_point(module_scope)
