# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/BattlePassRewardTakeOption.proto
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
    'genshin/packet/proto/BattlePassRewardTakeOption.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassRewardTag_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassRewardTag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/BattlePassRewardTakeOption.proto\x1a.genshin/packet/proto/BattlePassRewardTag.proto\"S\n\x1a\x42\x61ttlePassRewardTakeOption\x12\x12\n\noption_idx\x18\x04 \x01(\r\x12!\n\x03tag\x18\x0b \x01(\x0b\x32\x14.BattlePassRewardTagB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.BattlePassRewardTakeOption_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BATTLEPASSREWARDTAKEOPTION']._serialized_start=105
  _globals['_BATTLEPASSREWARDTAKEOPTION']._serialized_end=188
# @@protoc_insertion_point(module_scope)
