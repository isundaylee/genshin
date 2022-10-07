# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EnterRoguelikeDungeonNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RogueCellInfo_pb2 as genshin_dot_packet_dot_proto_dot_RogueCellInfo__pb2
from genshin.packet.proto import RoguelikeRuneRecord_pb2 as genshin_dot_packet_dot_proto_dot_RoguelikeRuneRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/EnterRoguelikeDungeonNotify.proto\x1a(genshin/packet/proto/RogueCellInfo.proto\x1a.genshin/packet/proto/RoguelikeRuneRecord.proto\"\xd5\x04\n\x1b\x45nterRoguelikeDungeonNotify\x12\x15\n\ris_mist_clear\x18\x0e \x01(\x08\x12 \n\x18\x64ungeon_weight_config_id\x18\x02 \x01(\r\x12.\n\x10rune_record_list\x18\x06 \x03(\x0b\x32\x14.RoguelikeRuneRecord\x12 \n\x18onstage_avatar_guid_list\x18\t \x03(\x04\x12\x17\n\x0eis_first_enter\x18\xcd\x01 \x01(\x08\x12\x1a\n\x12\x65xplored_cell_list\x18\x03 \x03(\r\x12\x44\n\rcell_info_map\x18\x0b \x03(\x0b\x32-.EnterRoguelikeDungeonNotify.CellInfoMapEntry\x12\x12\n\ndungeon_id\x18\x01 \x01(\r\x12 \n\x17refresh_cost_item_count\x18\xcf\x0f \x01(\r\x12\x1b\n\x13\x62onus_resource_prop\x18\r \x01(\x02\x12\x1d\n\x14revise_monster_level\x18\x85\x0c \x01(\r\x12\x10\n\x08stage_id\x18\x0f \x01(\r\x12\"\n\x1a\x62\x61\x63kstage_avatar_guid_list\x18\n \x03(\x04\x12\x13\n\x0b\x63ur_cell_id\x18\x0c \x01(\r\x12\x1c\n\x14refresh_cost_item_id\x18\x07 \x01(\r\x12\x11\n\tcur_level\x18\x08 \x01(\r\x1a\x42\n\x10\x43\x65llInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.RogueCellInfo:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_ENTERROGUELIKEDUNGEONNOTIFY = DESCRIPTOR.message_types_by_name['EnterRoguelikeDungeonNotify']
_ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY = _ENTERROGUELIKEDUNGEONNOTIFY.nested_types_by_name['CellInfoMapEntry']
EnterRoguelikeDungeonNotify = _reflection.GeneratedProtocolMessageType('EnterRoguelikeDungeonNotify', (_message.Message,), {

  'CellInfoMapEntry' : _reflection.GeneratedProtocolMessageType('CellInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.EnterRoguelikeDungeonNotify_pb2'
    # @@protoc_insertion_point(class_scope:EnterRoguelikeDungeonNotify.CellInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _ENTERROGUELIKEDUNGEONNOTIFY,
  '__module__' : 'genshin.packet.proto.EnterRoguelikeDungeonNotify_pb2'
  # @@protoc_insertion_point(class_scope:EnterRoguelikeDungeonNotify)
  })
_sym_db.RegisterMessage(EnterRoguelikeDungeonNotify)
_sym_db.RegisterMessage(EnterRoguelikeDungeonNotify.CellInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY._options = None
  _ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY._serialized_options = b'8\001'
  _ENTERROGUELIKEDUNGEONNOTIFY._serialized_start=149
  _ENTERROGUELIKEDUNGEONNOTIFY._serialized_end=746
  _ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY._serialized_start=680
  _ENTERROGUELIKEDUNGEONNOTIFY_CELLINFOMAPENTRY._serialized_end=746
# @@protoc_insertion_point(module_scope)