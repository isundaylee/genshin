# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EntityRendererChangedInfo.proto
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
    'genshin/packet/proto/EntityRendererChangedInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/EntityRendererChangedInfo.proto\"\xce\x01\n\x19\x45ntityRendererChangedInfo\x12K\n\x11\x63hanged_renderers\x18\x01 \x03(\x0b\x32\x30.EntityRendererChangedInfo.ChangedRenderersEntry\x12\x18\n\x10visibility_count\x18\x02 \x01(\r\x12\x11\n\tis_cached\x18\x03 \x01(\x08\x1a\x37\n\x15\x43hangedRenderersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EntityRendererChangedInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ENTITYRENDERERCHANGEDINFO_CHANGEDRENDERERSENTRY']._loaded_options = None
  _globals['_ENTITYRENDERERCHANGEDINFO_CHANGEDRENDERERSENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYRENDERERCHANGEDINFO']._serialized_start=57
  _globals['_ENTITYRENDERERCHANGEDINFO']._serialized_end=263
  _globals['_ENTITYRENDERERCHANGEDINFO_CHANGEDRENDERERSENTRY']._serialized_start=208
  _globals['_ENTITYRENDERERCHANGEDINFO_CHANGEDRENDERERSENTRY']._serialized_end=263
# @@protoc_insertion_point(module_scope)
