# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AvatarPropNotify.proto
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
    'genshin/packet/proto/AvatarPropNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/AvatarPropNotify.proto\"\x89\x01\n\x10\x41vatarPropNotify\x12\x13\n\x0b\x61vatar_guid\x18\x06 \x01(\x04\x12\x30\n\x08prop_map\x18\x08 \x03(\x0b\x32\x1e.AvatarPropNotify.PropMapEntry\x1a.\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AvatarPropNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_AVATARPROPNOTIFY_PROPMAPENTRY']._loaded_options = None
  _globals['_AVATARPROPNOTIFY_PROPMAPENTRY']._serialized_options = b'8\001'
  _globals['_AVATARPROPNOTIFY']._serialized_start=48
  _globals['_AVATARPROPNOTIFY']._serialized_end=185
  _globals['_AVATARPROPNOTIFY_PROPMAPENTRY']._serialized_start=139
  _globals['_AVATARPROPNOTIFY_PROPMAPENTRY']._serialized_end=185
# @@protoc_insertion_point(module_scope)
