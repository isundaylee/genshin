# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/WidgetSlotData.proto
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
    'genshin/packet/proto/WidgetSlotData.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WidgetSlotTag_pb2 as genshin_dot_packet_dot_proto_dot_WidgetSlotTag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/WidgetSlotData.proto\x1a(genshin/packet/proto/WidgetSlotTag.proto\"k\n\x0eWidgetSlotData\x12\x1b\n\x03tag\x18\x01 \x01(\x0e\x32\x0e.WidgetSlotTag\x12\x13\n\x0bmaterial_id\x18\t \x01(\r\x12\x14\n\x0c\x63\x64_over_time\x18\x0b \x01(\r\x12\x11\n\tis_active\x18\x0c \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.WidgetSlotData_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_WIDGETSLOTDATA']._serialized_start=87
  _globals['_WIDGETSLOTDATA']._serialized_end=194
# @@protoc_insertion_point(module_scope)
