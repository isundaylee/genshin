# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RogueStageInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RoguelikeRuneRecord_pb2 as genshin_dot_packet_dot_proto_dot_RoguelikeRuneRecord__pb2
from genshin.packet.proto import RogueShowAvatarTeamInfo_pb2 as genshin_dot_packet_dot_proto_dot_RogueShowAvatarTeamInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/RogueStageInfo.proto\x1a.genshin/packet/proto/RoguelikeRuneRecord.proto\x1a\x32genshin/packet/proto/RogueShowAvatarTeamInfo.proto\"\x9a\x03\n\x0eRogueStageInfo\x12-\n\x0b\x61vatar_team\x18\x02 \x01(\x0b\x32\x18.RogueShowAvatarTeamInfo\x12\x11\n\tis_passed\x18\x05 \x01(\x08\x12\x10\n\x08stage_id\x18\x07 \x01(\r\x12\x1d\n\x14revise_monster_level\x18\xcd\x01 \x01(\r\x12.\n\x10rune_record_list\x18\x06 \x03(\x0b\x32\x14.RoguelikeRuneRecord\x12\x0f\n\x07is_open\x18\x01 \x01(\x08\x12\x11\n\tcur_level\x18\x04 \x01(\r\x12\x1a\n\x11\x63\x61\x63hed_coin_c_num\x18\x81\x0b \x01(\r\x12\x17\n\x0fis_taken_reward\x18\x0b \x01(\x08\x12\x14\n\x0cis_in_combat\x18\x0c \x01(\x08\x12\x19\n\x11\x63\x61\x63hed_coin_b_num\x18\x0e \x01(\r\x12\x18\n\x10\x65xplore_cell_num\x18\x0f \x01(\r\x12\x12\n\ncoin_c_num\x18\x08 \x01(\r\x12\x13\n\x0bis_explored\x18\t \x01(\x08\x12\x18\n\x10max_passed_level\x18\x03 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_ROGUESTAGEINFO = DESCRIPTOR.message_types_by_name['RogueStageInfo']
RogueStageInfo = _reflection.GeneratedProtocolMessageType('RogueStageInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROGUESTAGEINFO,
  '__module__' : 'genshin.packet.proto.RogueStageInfo_pb2'
  # @@protoc_insertion_point(class_scope:RogueStageInfo)
  })
_sym_db.RegisterMessage(RogueStageInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ROGUESTAGEINFO._serialized_start=146
  _ROGUESTAGEINFO._serialized_end=556
# @@protoc_insertion_point(module_scope)