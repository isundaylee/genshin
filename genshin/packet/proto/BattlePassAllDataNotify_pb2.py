# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/BattlePassAllDataNotify.proto
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
    'genshin/packet/proto/BattlePassAllDataNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassSchedule_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassSchedule__pb2
from genshin.packet.proto import BattlePassMission_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassMission__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/BattlePassAllDataNotify.proto\x1a-genshin/packet/proto/BattlePassSchedule.proto\x1a,genshin/packet/proto/BattlePassMission.proto\"\xce\x01\n\x17\x42\x61ttlePassAllDataNotify\x12\x19\n\x11have_cur_schedule\x18\x01 \x01(\x08\x12)\n\x0c\x63ur_schedule\x18\x03 \x01(\x0b\x32\x13.BattlePassSchedule\x12\x13\n\x0bHNDKICJJANM\x18\x08 \x01(\x08\x12\x11\n\tis_viewed\x18\t \x01(\x08\x12(\n\x0cmission_list\x18\x0c \x03(\x0b\x32\x12.BattlePassMission\x12\x1b\n\x13\x64\x65\x66\x61ult_reward_type\x18\r \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.BattlePassAllDataNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BATTLEPASSALLDATANOTIFY']._serialized_start=148
  _globals['_BATTLEPASSALLDATANOTIFY']._serialized_end=354
# @@protoc_insertion_point(module_scope)
