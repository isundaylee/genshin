# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/MainCoop.proto
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
    'genshin/packet/proto/MainCoop.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#genshin/packet/proto/MainCoop.proto\"\xd6\x03\n\x08MainCoop\x12\x17\n\x0fself_confidence\x18\x05 \x01(\r\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x10.MainCoop.Status\x12\x1a\n\x12save_point_id_list\x18\t \x03(\r\x12\n\n\x02id\x18\x06 \x01(\r\x12/\n\x0bGEHNFJEPCJL\x18\x0c \x03(\x0b\x32\x1a.MainCoop.GEHNFJEPCJLEntry\x12/\n\x0bGDBKBKACDFO\x18\x08 \x03(\x0b\x32\x1a.MainCoop.GDBKBKACDFOEntry\x12\x35\n\x0fseen_ending_map\x18\x03 \x03(\x0b\x32\x1c.MainCoop.SeenEndingMapEntry\x1a\x32\n\x10GEHNFJEPCJLEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x32\n\x10GDBKBKACDFOEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x34\n\x12SeenEndingMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"0\n\x06Status\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.MainCoop_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_MAINCOOP_GEHNFJEPCJLENTRY']._loaded_options = None
  _globals['_MAINCOOP_GEHNFJEPCJLENTRY']._serialized_options = b'8\001'
  _globals['_MAINCOOP_GDBKBKACDFOENTRY']._loaded_options = None
  _globals['_MAINCOOP_GDBKBKACDFOENTRY']._serialized_options = b'8\001'
  _globals['_MAINCOOP_SEENENDINGMAPENTRY']._loaded_options = None
  _globals['_MAINCOOP_SEENENDINGMAPENTRY']._serialized_options = b'8\001'
  _globals['_MAINCOOP']._serialized_start=40
  _globals['_MAINCOOP']._serialized_end=510
  _globals['_MAINCOOP_GEHNFJEPCJLENTRY']._serialized_start=304
  _globals['_MAINCOOP_GEHNFJEPCJLENTRY']._serialized_end=354
  _globals['_MAINCOOP_GDBKBKACDFOENTRY']._serialized_start=356
  _globals['_MAINCOOP_GDBKBKACDFOENTRY']._serialized_end=406
  _globals['_MAINCOOP_SEENENDINGMAPENTRY']._serialized_start=408
  _globals['_MAINCOOP_SEENENDINGMAPENTRY']._serialized_end=460
  _globals['_MAINCOOP_STATUS']._serialized_start=462
  _globals['_MAINCOOP_STATUS']._serialized_end=510
# @@protoc_insertion_point(module_scope)
