# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/WidgetDoBagReq.proto
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
    'genshin/packet/proto/WidgetDoBagReq.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WidgetCreateLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCreateLocationInfo__pb2
from genshin.packet.proto import WidgetCreatorInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCreatorInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/WidgetDoBagReq.proto\x1a\x33genshin/packet/proto/WidgetCreateLocationInfo.proto\x1a,genshin/packet/proto/WidgetCreatorInfo.proto\"\x99\x01\n\x0eWidgetDoBagReq\x12\x13\n\x0bmaterial_id\x18\x0b \x01(\r\x12\x33\n\rlocation_info\x18\xdb\r \x01(\x0b\x32\x19.WidgetCreateLocationInfoH\x00\x12\x32\n\x13widget_creator_info\x18\xda\x06 \x01(\x0b\x32\x12.WidgetCreatorInfoH\x00\x42\t\n\x07op_infoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.WidgetDoBagReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_WIDGETDOBAGREQ']._serialized_start=145
  _globals['_WIDGETDOBAGREQ']._serialized_end=298
# @@protoc_insertion_point(module_scope)
