# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ServerBuff.proto
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
    'genshin/packet/proto/ServerBuff.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/ServerBuff.proto\"\x91\x01\n\nServerBuff\x12\x17\n\x0fserver_buff_uid\x18\x01 \x01(\r\x12\x16\n\x0eserver_buff_id\x18\x02 \x01(\r\x12\x18\n\x10server_buff_type\x18\x03 \x01(\r\x12\x1d\n\x15instanced_modifier_id\x18\x04 \x01(\r\x12\x19\n\x11is_modifier_added\x18\x05 \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ServerBuff_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_SERVERBUFF']._serialized_start=42
  _globals['_SERVERBUFF']._serialized_end=187
# @@protoc_insertion_point(module_scope)
