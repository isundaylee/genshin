# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/DailyTaskInfo.proto
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
    'genshin/packet/proto/DailyTaskInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/DailyTaskInfo.proto\"y\n\rDailyTaskInfo\x12\x13\n\x0bis_finished\x18\r \x01(\x08\x12\x10\n\x08progress\x18\x08 \x01(\r\x12\x15\n\rdaily_task_id\x18\x0c \x01(\r\x12\x17\n\x0f\x66inish_progress\x18\x0b \x01(\r\x12\x11\n\treward_id\x18\n \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.DailyTaskInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_DAILYTASKINFO']._serialized_start=44
  _globals['_DAILYTASKINFO']._serialized_end=165
# @@protoc_insertion_point(module_scope)
