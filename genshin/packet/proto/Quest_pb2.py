# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Quest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n genshin/packet/proto/Quest.proto\"\xf1\x03\n\x05Quest\x12\x10\n\x08quest_id\x18\x01 \x01(\r\x12\r\n\x05state\x18\x02 \x01(\r\x12\x12\n\nstart_time\x18\x04 \x01(\r\x12\x11\n\tis_random\x18\x05 \x01(\x08\x12\x17\n\x0fparent_quest_id\x18\x06 \x01(\r\x12\x17\n\x0fquest_config_id\x18\x07 \x01(\r\x12\x17\n\x0fstart_game_time\x18\x08 \x01(\r\x12\x13\n\x0b\x61\x63\x63\x65pt_time\x18\t \x01(\r\x12\x17\n\x0flacked_npc_list\x18\n \x03(\r\x12\x1c\n\x14\x66inish_progress_list\x18\x0b \x03(\r\x12\x1a\n\x12\x66\x61il_progress_list\x18\x0c \x03(\r\x12\x30\n\x0elacked_npc_map\x18\r \x03(\x0b\x32\x18.Quest.LackedNpcMapEntry\x12\x19\n\x11lacked_place_list\x18\x0e \x03(\r\x12\x34\n\x10lacked_place_map\x18\x0f \x03(\x0b\x32\x1a.Quest.LackedPlaceMapEntry\x1a\x33\n\x11LackedNpcMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13LackedPlaceMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_QUEST = DESCRIPTOR.message_types_by_name['Quest']
_QUEST_LACKEDNPCMAPENTRY = _QUEST.nested_types_by_name['LackedNpcMapEntry']
_QUEST_LACKEDPLACEMAPENTRY = _QUEST.nested_types_by_name['LackedPlaceMapEntry']
Quest = _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), {

  'LackedNpcMapEntry' : _reflection.GeneratedProtocolMessageType('LackedNpcMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUEST_LACKEDNPCMAPENTRY,
    '__module__' : 'genshin.packet.proto.Quest_pb2'
    # @@protoc_insertion_point(class_scope:Quest.LackedNpcMapEntry)
    })
  ,

  'LackedPlaceMapEntry' : _reflection.GeneratedProtocolMessageType('LackedPlaceMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUEST_LACKEDPLACEMAPENTRY,
    '__module__' : 'genshin.packet.proto.Quest_pb2'
    # @@protoc_insertion_point(class_scope:Quest.LackedPlaceMapEntry)
    })
  ,
  'DESCRIPTOR' : _QUEST,
  '__module__' : 'genshin.packet.proto.Quest_pb2'
  # @@protoc_insertion_point(class_scope:Quest)
  })
_sym_db.RegisterMessage(Quest)
_sym_db.RegisterMessage(Quest.LackedNpcMapEntry)
_sym_db.RegisterMessage(Quest.LackedPlaceMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _QUEST_LACKEDNPCMAPENTRY._options = None
  _QUEST_LACKEDNPCMAPENTRY._serialized_options = b'8\001'
  _QUEST_LACKEDPLACEMAPENTRY._options = None
  _QUEST_LACKEDPLACEMAPENTRY._serialized_options = b'8\001'
  _QUEST._serialized_start=37
  _QUEST._serialized_end=534
  _QUEST_LACKEDNPCMAPENTRY._serialized_start=428
  _QUEST_LACKEDNPCMAPENTRY._serialized_end=479
  _QUEST_LACKEDPLACEMAPENTRY._serialized_start=481
  _QUEST_LACKEDPLACEMAPENTRY._serialized_end=534
# @@protoc_insertion_point(module_scope)
