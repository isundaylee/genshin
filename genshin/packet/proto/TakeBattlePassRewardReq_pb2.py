# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/TakeBattlePassRewardReq.proto
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
    'genshin/packet/proto/TakeBattlePassRewardReq.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassRewardTakeOption_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassRewardTakeOption__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/TakeBattlePassRewardReq.proto\x1a\x35genshin/packet/proto/BattlePassRewardTakeOption.proto\"P\n\x17TakeBattlePassRewardReq\x12\x35\n\x10take_option_list\x18\x08 \x03(\x0b\x32\x1b.BattlePassRewardTakeOptionB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.TakeBattlePassRewardReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_TAKEBATTLEPASSREWARDREQ']._serialized_start=109
  _globals['_TAKEBATTLEPASSREWARDREQ']._serialized_end=189
# @@protoc_insertion_point(module_scope)
