# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/SceneEntityUpdateNotify.proto
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
    'genshin/packet/proto/SceneEntityUpdateNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SceneEntityInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneEntityInfo__pb2
from genshin.packet.proto import VisionType_pb2 as genshin_dot_packet_dot_proto_dot_VisionType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/SceneEntityUpdateNotify.proto\x1a*genshin/packet/proto/SceneEntityInfo.proto\x1a%genshin/packet/proto/VisionType.proto\"q\n\x17SceneEntityUpdateNotify\x12%\n\x0b\x65ntity_list\x18\x08 \x03(\x0b\x32\x10.SceneEntityInfo\x12 \n\x0b\x61ppear_type\x18\x0b \x01(\x0e\x32\x0b.VisionType\x12\r\n\x05param\x18\x04 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.SceneEntityUpdateNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_SCENEENTITYUPDATENOTIFY']._serialized_start=137
  _globals['_SCENEENTITYUPDATENOTIFY']._serialized_end=250
# @@protoc_insertion_point(module_scope)
