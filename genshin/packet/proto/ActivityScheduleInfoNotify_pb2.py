# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ActivityScheduleInfoNotify.proto
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
    'genshin/packet/proto/ActivityScheduleInfoNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ActivityScheduleInfo_pb2 as genshin_dot_packet_dot_proto_dot_ActivityScheduleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/ActivityScheduleInfoNotify.proto\x1a/genshin/packet/proto/ActivityScheduleInfo.proto\"t\n\x1a\x41\x63tivityScheduleInfoNotify\x12\x1f\n\x17remain_fly_sea_lamp_num\x18\x01 \x01(\r\x12\x35\n\x16\x61\x63tivity_schedule_list\x18\x0c \x03(\x0b\x32\x15.ActivityScheduleInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ActivityScheduleInfoNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ACTIVITYSCHEDULEINFONOTIFY']._serialized_start=106
  _globals['_ACTIVITYSCHEDULEINFONOTIFY']._serialized_end=222
# @@protoc_insertion_point(module_scope)
