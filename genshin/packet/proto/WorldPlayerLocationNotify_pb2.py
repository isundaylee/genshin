# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/WorldPlayerLocationNotify.proto
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
    'genshin/packet/proto/WorldPlayerLocationNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlayerLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlayerLocationInfo__pb2
from genshin.packet.proto import PlayerWorldLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlayerWorldLocationInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/WorldPlayerLocationNotify.proto\x1a-genshin/packet/proto/PlayerLocationInfo.proto\x1a\x32genshin/packet/proto/PlayerWorldLocationInfo.proto\"\x82\x01\n\x19WorldPlayerLocationNotify\x12,\n\x0fplayer_loc_list\x18\x03 \x03(\x0b\x32\x13.PlayerLocationInfo\x12\x37\n\x15player_world_loc_list\x18\x0b \x03(\x0b\x32\x18.PlayerWorldLocationInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.WorldPlayerLocationNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_WORLDPLAYERLOCATIONNOTIFY']._serialized_start=156
  _globals['_WORLDPLAYERLOCATIONNOTIFY']._serialized_end=286
# @@protoc_insertion_point(module_scope)
