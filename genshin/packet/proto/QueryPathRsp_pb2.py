# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/QueryPathRsp.proto
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
    'genshin/packet/proto/QueryPathRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2
from genshin.packet.proto import PathStatusType_pb2 as genshin_dot_packet_dot_proto_dot_PathStatusType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/QueryPathRsp.proto\x1a!genshin/packet/proto/Vector.proto\x1a)genshin/packet/proto/PathStatusType.proto\"r\n\x0cQueryPathRsp\x12\x18\n\x07\x63orners\x18\x02 \x03(\x0b\x32\x07.Vector\x12\x10\n\x08query_id\x18\x05 \x01(\x05\x12\x0f\n\x07retcode\x18\x07 \x01(\x05\x12%\n\x0cquery_status\x18\x0f \x01(\x0e\x32\x0f.PathStatusTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.QueryPathRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_QUERYPATHRSP']._serialized_start=121
  _globals['_QUERYPATHRSP']._serialized_end=235
# @@protoc_insertion_point(module_scope)
