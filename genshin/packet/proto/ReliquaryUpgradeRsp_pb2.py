# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ReliquaryUpgradeRsp.proto
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
    'genshin/packet/proto/ReliquaryUpgradeRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/ReliquaryUpgradeRsp.proto\"\xbe\x01\n\x13ReliquaryUpgradeRsp\x12\x1d\n\x15target_reliquary_guid\x18\x0c \x01(\x04\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x12\x15\n\rpower_up_rate\x18\x0b \x01(\r\x12\x11\n\tcur_level\x18\x07 \x01(\r\x12\x11\n\told_level\x18\x0e \x01(\r\x12\x1c\n\x14\x63ur_append_prop_list\x18\x01 \x03(\r\x12\x1c\n\x14old_append_prop_list\x18\x08 \x03(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ReliquaryUpgradeRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_RELIQUARYUPGRADERSP']._serialized_start=51
  _globals['_RELIQUARYUPGRADERSP']._serialized_end=241
# @@protoc_insertion_point(module_scope)
