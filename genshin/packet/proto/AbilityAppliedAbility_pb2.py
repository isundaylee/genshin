# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AbilityAppliedAbility.proto
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
    'genshin/packet/proto/AbilityAppliedAbility.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityString_pb2 as genshin_dot_packet_dot_proto_dot_AbilityString__pb2
from genshin.packet.proto import AbilityScalarValueEntry_pb2 as genshin_dot_packet_dot_proto_dot_AbilityScalarValueEntry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/AbilityAppliedAbility.proto\x1a(genshin/packet/proto/AbilityString.proto\x1a\x32genshin/packet/proto/AbilityScalarValueEntry.proto\"\xb5\x01\n\x15\x41\x62ilityAppliedAbility\x12$\n\x0c\x61\x62ility_name\x18\x01 \x01(\x0b\x32\x0e.AbilityString\x12(\n\x10\x61\x62ility_override\x18\x02 \x01(\x0b\x32\x0e.AbilityString\x12.\n\x0coverride_map\x18\x03 \x03(\x0b\x32\x18.AbilityScalarValueEntry\x12\x1c\n\x14instanced_ability_id\x18\x04 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AbilityAppliedAbility_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ABILITYAPPLIEDABILITY']._serialized_start=147
  _globals['_ABILITYAPPLIEDABILITY']._serialized_end=328
# @@protoc_insertion_point(module_scope)
