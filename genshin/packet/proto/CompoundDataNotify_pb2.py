# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/CompoundDataNotify.proto
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
    'genshin/packet/proto/CompoundDataNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CompoundQueueData_pb2 as genshin_dot_packet_dot_proto_dot_CompoundQueueData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/CompoundDataNotify.proto\x1a,genshin/packet/proto/CompoundQueueData.proto\"c\n\x12\x43ompoundDataNotify\x12\x31\n\x15\x63ompoundQueueDataList\x18\x03 \x03(\x0b\x32\x12.CompoundQueueData\x12\x1a\n\x12unlockCompoundList\x18\x0e \x03(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.CompoundDataNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_COMPOUNDDATANOTIFY']._serialized_start=95
  _globals['_COMPOUNDDATANOTIFY']._serialized_end=194
# @@protoc_insertion_point(module_scope)
