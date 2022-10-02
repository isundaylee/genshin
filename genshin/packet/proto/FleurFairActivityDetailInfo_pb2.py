# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FleurFairActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FleurFairChapterInfo_pb2 as genshin_dot_packet_dot_proto_dot_FleurFairChapterInfo__pb2
from genshin.packet.proto import FleurFairDungeonSectionInfo_pb2 as genshin_dot_packet_dot_proto_dot_FleurFairDungeonSectionInfo__pb2
from genshin.packet.proto import FleurFairMinigameInfo_pb2 as genshin_dot_packet_dot_proto_dot_FleurFairMinigameInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/FleurFairActivityDetailInfo.proto\x1a/genshin/packet/proto/FleurFairChapterInfo.proto\x1a\x36genshin/packet/proto/FleurFairDungeonSectionInfo.proto\x1a\x30genshin/packet/proto/FleurFairMinigameInfo.proto\"\xb2\x04\n\x1b\x46leurFairActivityDetailInfo\x12\x19\n\x11is_content_closed\x18\x04 \x01(\x08\x12 \n\x18\x64ungeon_punish_over_time\x18\x06 \x01(\r\x12\x1a\n\x12\x63ontent_close_time\x18\x0f \x01(\r\x12\x16\n\x0eobtained_token\x18\r \x01(\r\x12\x30\n\x11\x63hapter_info_list\x18\x0e \x03(\x0b\x32\x15.FleurFairChapterInfo\x12L\n\x11minigame_info_map\x18\t \x03(\x0b\x32\x31.FleurFairActivityDetailInfo.MinigameInfoMapEntry\x12Y\n\x18\x64ungeon_section_info_map\x18\x03 \x03(\x0b\x32\x37.FleurFairActivityDetailInfo.DungeonSectionInfoMapEntry\x12\x1b\n\x13is_dungeon_unlocked\x18\x0b \x01(\x08\x1aN\n\x14MinigameInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.FleurFairMinigameInfo:\x02\x38\x01\x1aZ\n\x1a\x44ungeonSectionInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.FleurFairDungeonSectionInfo:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_FLEURFAIRACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['FleurFairActivityDetailInfo']
_FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY = _FLEURFAIRACTIVITYDETAILINFO.nested_types_by_name['MinigameInfoMapEntry']
_FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY = _FLEURFAIRACTIVITYDETAILINFO.nested_types_by_name['DungeonSectionInfoMapEntry']
FleurFairActivityDetailInfo = _reflection.GeneratedProtocolMessageType('FleurFairActivityDetailInfo', (_message.Message,), {

  'MinigameInfoMapEntry' : _reflection.GeneratedProtocolMessageType('MinigameInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.FleurFairActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:FleurFairActivityDetailInfo.MinigameInfoMapEntry)
    })
  ,

  'DungeonSectionInfoMapEntry' : _reflection.GeneratedProtocolMessageType('DungeonSectionInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.FleurFairActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:FleurFairActivityDetailInfo.DungeonSectionInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _FLEURFAIRACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.FleurFairActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:FleurFairActivityDetailInfo)
  })
_sym_db.RegisterMessage(FleurFairActivityDetailInfo)
_sym_db.RegisterMessage(FleurFairActivityDetailInfo.MinigameInfoMapEntry)
_sym_db.RegisterMessage(FleurFairActivityDetailInfo.DungeonSectionInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._options = None
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._serialized_options = b'8\001'
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._options = None
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._serialized_options = b'8\001'
  _FLEURFAIRACTIVITYDETAILINFO._serialized_start=214
  _FLEURFAIRACTIVITYDETAILINFO._serialized_end=776
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._serialized_start=606
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._serialized_end=684
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._serialized_start=686
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._serialized_end=776
# @@protoc_insertion_point(module_scope)
