# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/PlayerInvestigationAllInfoNotify.proto
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
    'genshin/packet/proto/PlayerInvestigationAllInfoNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import InvestigationTarget_pb2 as genshin_dot_packet_dot_proto_dot_InvestigationTarget__pb2
from genshin.packet.proto import Investigation_pb2 as genshin_dot_packet_dot_proto_dot_Investigation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;genshin/packet/proto/PlayerInvestigationAllInfoNotify.proto\x1a.genshin/packet/proto/InvestigationTarget.proto\x1a(genshin/packet/proto/Investigation.proto\"\x87\x01\n PlayerInvestigationAllInfoNotify\x12\x37\n\x19investigation_target_list\x18\x08 \x03(\x0b\x32\x14.InvestigationTarget\x12*\n\x12investigation_list\x18\t \x03(\x0b\x32\x0e.InvestigationB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.PlayerInvestigationAllInfoNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_PLAYERINVESTIGATIONALLINFONOTIFY']._serialized_start=154
  _globals['_PLAYERINVESTIGATIONALLINFONOTIFY']._serialized_end=289
# @@protoc_insertion_point(module_scope)
