# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/PlatformStopRouteNotify.proto
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
    'genshin/packet/proto/PlatformStopRouteNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlatformInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlatformInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/PlatformStopRouteNotify.proto\x1a\'genshin/packet/proto/PlatformInfo.proto\"a\n\x17PlatformStopRouteNotify\x12\x12\n\nscene_time\x18\x02 \x01(\r\x12\x1f\n\x08platform\x18\x05 \x01(\x0b\x32\r.PlatformInfo\x12\x11\n\tentity_id\x18\x0c \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.PlatformStopRouteNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_PLATFORMSTOPROUTENOTIFY']._serialized_start=95
  _globals['_PLATFORMSTOPROUTENOTIFY']._serialized_end=192
# @@protoc_insertion_point(module_scope)
