# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AnnounceData.proto
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
    'genshin/packet/proto/AnnounceData.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/AnnounceData.proto\"\x87\x02\n\x0c\x41nnounceData\x12\x10\n\x08\x65nd_time\x18\x01 \x01(\r\x12\x1c\n\x14\x63ount_down_frequency\x18\x03 \x01(\r\x12\x1c\n\x14\x64ungeon_confirm_text\x18\x06 \x01(\t\x12\x17\n\x0f\x63ount_down_text\x18\x07 \x01(\t\x12\x1f\n\x17\x63\x65nter_system_frequency\x18\x08 \x01(\r\x12,\n$is_center_system_last5_every_minutes\x18\n \x01(\x08\x12\x1a\n\x12\x63\x65nter_system_text\x18\x0c \x01(\t\x12\x12\n\nbegin_time\x18\r \x01(\r\x12\x11\n\tconfig_id\x18\x0e \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AnnounceData_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ANNOUNCEDATA']._serialized_start=44
  _globals['_ANNOUNCEDATA']._serialized_end=307
# @@protoc_insertion_point(module_scope)
