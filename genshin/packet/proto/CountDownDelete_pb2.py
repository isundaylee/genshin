# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/CountDownDelete.proto
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
    'genshin/packet/proto/CountDownDelete.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/CountDownDelete.proto\"\xaf\x01\n\x0f\x43ountDownDelete\x12\x43\n\x13\x64\x65lete_time_num_map\x18\x01 \x03(\x0b\x32&.CountDownDelete.DeleteTimeNumMapEntry\x12\x1e\n\x16\x63onfig_count_down_time\x18\x02 \x01(\r\x1a\x37\n\x15\x44\x65leteTimeNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.CountDownDelete_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_COUNTDOWNDELETE_DELETETIMENUMMAPENTRY']._loaded_options = None
  _globals['_COUNTDOWNDELETE_DELETETIMENUMMAPENTRY']._serialized_options = b'8\001'
  _globals['_COUNTDOWNDELETE']._serialized_start=47
  _globals['_COUNTDOWNDELETE']._serialized_end=222
  _globals['_COUNTDOWNDELETE_DELETETIMENUMMAPENTRY']._serialized_start=167
  _globals['_COUNTDOWNDELETE_DELETETIMENUMMAPENTRY']._serialized_end=222
# @@protoc_insertion_point(module_scope)
