# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ChallengeBrief.proto
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
    'genshin/packet/proto/ChallengeBrief.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/ChallengeBrief.proto\"i\n\x0e\x43hallengeBrief\x12\x17\n\x0f\x63hallenge_index\x18\x01 \x01(\r\x12\x12\n\nis_success\x18\x08 \x01(\x08\x12\x14\n\x0c\x63hallenge_id\x18\t \x01(\r\x12\x14\n\x0c\x63ur_progress\x18\x0c \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ChallengeBrief_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_CHALLENGEBRIEF']._serialized_start=45
  _globals['_CHALLENGEBRIEF']._serialized_end=150
# @@protoc_insertion_point(module_scope)