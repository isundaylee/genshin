# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonEntryBlockReason.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/DungeonEntryBlockReason.proto*\xb2\x01\n\x17\x44ungeonEntryBlockReason\x12#\n\x1f\x44UNGEON_ENTRY_BLOCK_REASON_NONE\x10\x00\x12$\n DUNGEON_ENTRY_BLOCK_REASON_LEVEL\x10\x01\x12$\n DUNGEON_ENTRY_BLOCK_REASON_QUEST\x10\x02\x12&\n\"DUNGEON_ENTRY_BLOCK_REASON_MULIPLE\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_DUNGEONENTRYBLOCKREASON = DESCRIPTOR.enum_types_by_name['DungeonEntryBlockReason']
DungeonEntryBlockReason = enum_type_wrapper.EnumTypeWrapper(_DUNGEONENTRYBLOCKREASON)
DUNGEON_ENTRY_BLOCK_REASON_NONE = 0
DUNGEON_ENTRY_BLOCK_REASON_LEVEL = 1
DUNGEON_ENTRY_BLOCK_REASON_QUEST = 2
DUNGEON_ENTRY_BLOCK_REASON_MULIPLE = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DUNGEONENTRYBLOCKREASON._serialized_start=55
  _DUNGEONENTRYBLOCKREASON._serialized_end=233
# @@protoc_insertion_point(module_scope)