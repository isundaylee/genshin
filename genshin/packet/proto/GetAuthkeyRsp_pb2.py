# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/GetAuthkeyRsp.proto
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
    'genshin/packet/proto/GetAuthkeyRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/GetAuthkeyRsp.proto\"\x7f\n\rGetAuthkeyRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x12\n\nauth_appid\x18\x02 \x01(\t\x12\x10\n\x08game_biz\x18\x03 \x01(\t\x12\x11\n\tsign_type\x18\x04 \x01(\r\x12\x13\n\x0b\x61uthkey_ver\x18\x07 \x01(\r\x12\x0f\n\x07\x61uthkey\x18\r \x01(\tB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.GetAuthkeyRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_GETAUTHKEYRSP']._serialized_start=44
  _globals['_GETAUTHKEYRSP']._serialized_end=171
# @@protoc_insertion_point(module_scope)
