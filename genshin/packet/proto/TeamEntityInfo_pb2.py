# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/TeamEntityInfo.proto
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
    'genshin/packet/proto/TeamEntityInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/TeamEntityInfo.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\"u\n\x0eTeamEntityInfo\x12\x16\n\x0eteam_entity_id\x18\t \x01(\r\x12\x30\n\x11team_ability_info\x18\r \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x19\n\x11\x61uthority_peer_id\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.TeamEntityInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_TEAMENTITYINFO']._serialized_start=94
  _globals['_TEAMENTITYINFO']._serialized_end=211
# @@protoc_insertion_point(module_scope)
