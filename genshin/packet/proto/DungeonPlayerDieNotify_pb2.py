# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonPlayerDieNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlayerDieType_pb2 as genshin_dot_packet_dot_proto_dot_PlayerDieType__pb2
from genshin.packet.proto import StrengthenPointData_pb2 as genshin_dot_packet_dot_proto_dot_StrengthenPointData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/DungeonPlayerDieNotify.proto\x1a(genshin/packet/proto/PlayerDieType.proto\x1a.genshin/packet/proto/StrengthenPointData.proto\"\xf5\x02\n\x16\x44ungeonPlayerDieNotify\x12V\n\x19strengthen_point_data_map\x18\x0f \x03(\x0b\x32\x33.DungeonPlayerDieNotify.StrengthenPointDataMapEntry\x12\x11\n\twait_time\x18\x01 \x01(\r\x12\x12\n\ndungeon_id\x18\t \x01(\r\x12\x1a\n\x12murderer_entity_id\x18\r \x01(\r\x12 \n\x08\x64ie_type\x18\x03 \x01(\x0e\x32\x0e.PlayerDieType\x12\x14\n\x0crevive_count\x18\x06 \x01(\r\x12\x14\n\nmonster_id\x18\x04 \x01(\rH\x00\x12\x13\n\tgadget_id\x18\x08 \x01(\rH\x00\x1aS\n\x1bStrengthenPointDataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.StrengthenPointData:\x02\x38\x01\x42\x08\n\x06\x65ntityB\x16\n\x14org.sorapointa.protob\x06proto3')



_DUNGEONPLAYERDIENOTIFY = DESCRIPTOR.message_types_by_name['DungeonPlayerDieNotify']
_DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY = _DUNGEONPLAYERDIENOTIFY.nested_types_by_name['StrengthenPointDataMapEntry']
DungeonPlayerDieNotify = _reflection.GeneratedProtocolMessageType('DungeonPlayerDieNotify', (_message.Message,), {

  'StrengthenPointDataMapEntry' : _reflection.GeneratedProtocolMessageType('StrengthenPointDataMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY,
    '__module__' : 'genshin.packet.proto.DungeonPlayerDieNotify_pb2'
    # @@protoc_insertion_point(class_scope:DungeonPlayerDieNotify.StrengthenPointDataMapEntry)
    })
  ,
  'DESCRIPTOR' : _DUNGEONPLAYERDIENOTIFY,
  '__module__' : 'genshin.packet.proto.DungeonPlayerDieNotify_pb2'
  # @@protoc_insertion_point(class_scope:DungeonPlayerDieNotify)
  })
_sym_db.RegisterMessage(DungeonPlayerDieNotify)
_sym_db.RegisterMessage(DungeonPlayerDieNotify.StrengthenPointDataMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY._options = None
  _DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_options = b'8\001'
  _DUNGEONPLAYERDIENOTIFY._serialized_start=144
  _DUNGEONPLAYERDIENOTIFY._serialized_end=517
  _DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_start=424
  _DUNGEONPLAYERDIENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_end=507
# @@protoc_insertion_point(module_scope)
