# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonEntryInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WeeklyBossResinDiscountInfo_pb2 as genshin_dot_packet_dot_proto_dot_WeeklyBossResinDiscountInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/DungeonEntryInfo.proto\x1a\x36genshin/packet/proto/WeeklyBossResinDiscountInfo.proto\"\x89\x02\n\x10\x44ungeonEntryInfo\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\r\x12\x12\n\ndungeon_id\x18\x05 \x01(\r\x12\x16\n\x0e\x62oss_chest_num\x18\x0c \x01(\r\x12\x1a\n\x12max_boss_chest_num\x18\r \x01(\r\x12\x19\n\x11next_refresh_time\x18\x0b \x01(\r\x12\x45\n\x1fweekly_boss_resin_discount_info\x18\t \x01(\x0b\x32\x1c.WeeklyBossResinDiscountInfo\x12\x12\n\nstart_time\x18\x0f \x01(\r\x12\x11\n\tis_passed\x18\x04 \x01(\x08\x12\x12\n\nleft_times\x18\x07 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_DUNGEONENTRYINFO = DESCRIPTOR.message_types_by_name['DungeonEntryInfo']
DungeonEntryInfo = _reflection.GeneratedProtocolMessageType('DungeonEntryInfo', (_message.Message,), {
  'DESCRIPTOR' : _DUNGEONENTRYINFO,
  '__module__' : 'genshin.packet.proto.DungeonEntryInfo_pb2'
  # @@protoc_insertion_point(class_scope:DungeonEntryInfo)
  })
_sym_db.RegisterMessage(DungeonEntryInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _DUNGEONENTRYINFO._serialized_start=104
  _DUNGEONENTRYINFO._serialized_end=369
# @@protoc_insertion_point(module_scope)
