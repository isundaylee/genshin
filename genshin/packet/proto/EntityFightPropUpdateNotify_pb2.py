# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EntityFightPropUpdateNotify.proto
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
    'genshin/packet/proto/EntityFightPropUpdateNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/EntityFightPropUpdateNotify.proto\"\xad\x01\n\x1b\x45ntityFightPropUpdateNotify\x12\x46\n\x0e\x66ight_prop_map\x18\r \x03(\x0b\x32..EntityFightPropUpdateNotify.FightPropMapEntry\x12\x11\n\tentity_id\x18\x0e \x01(\r\x1a\x33\n\x11\x46ightPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EntityFightPropUpdateNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY_FIGHTPROPMAPENTRY']._loaded_options = None
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY_FIGHTPROPMAPENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY']._serialized_start=59
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY']._serialized_end=232
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY_FIGHTPROPMAPENTRY']._serialized_start=181
  _globals['_ENTITYFIGHTPROPUPDATENOTIFY_FIGHTPROPMAPENTRY']._serialized_end=232
# @@protoc_insertion_point(module_scope)
