# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/PingReq.proto
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
    'genshin/packet/proto/PingReq.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"genshin/packet/proto/PingReq.proto\"\xa5\x01\n\x07PingReq\x12\x13\n\x0bPDHFGJIBCLA\x18\r \x01(\x0c\x12\x0f\n\x07sc_data\x18\x02 \x01(\x0c\x12\x13\n\x0bNHLLKPHMFGP\x18\x03 \x01(\x04\x12\x17\n\x0ftotal_tick_time\x18\x07 \x01(\x01\x12\x13\n\x0b\x63lient_time\x18\x04 \x01(\r\x12\x0f\n\x07ue_time\x18\x08 \x01(\x02\x12\x13\n\x0b\x44\x46\x41LBBBCFMO\x18\n \x01(\r\x12\x0b\n\x03seq\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.PingReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_PINGREQ']._serialized_start=39
  _globals['_PINGREQ']._serialized_end=204
# @@protoc_insertion_point(module_scope)
