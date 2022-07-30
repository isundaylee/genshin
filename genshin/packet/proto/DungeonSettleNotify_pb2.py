# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChannelerSlabLoopDungeonResultInfo_pb2 as genshin_dot_packet_dot_proto_dot_ChannelerSlabLoopDungeonResultInfo__pb2
from genshin.packet.proto import CrystalLinkSettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_CrystalLinkSettleInfo__pb2
from genshin.packet.proto import DungeonSettleExhibitionInfo_pb2 as genshin_dot_packet_dot_proto_dot_DungeonSettleExhibitionInfo__pb2
from genshin.packet.proto import EffigyChallengeDungeonResultInfo_pb2 as genshin_dot_packet_dot_proto_dot_EffigyChallengeDungeonResultInfo__pb2
from genshin.packet.proto import ParamList_pb2 as genshin_dot_packet_dot_proto_dot_ParamList__pb2
from genshin.packet.proto import RoguelikeDungeonSettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_RoguelikeDungeonSettleInfo__pb2
from genshin.packet.proto import StrengthenPointData_pb2 as genshin_dot_packet_dot_proto_dot_StrengthenPointData__pb2
from genshin.packet.proto import SummerTimeV2DungeonSettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_SummerTimeV2DungeonSettleInfo__pb2
from genshin.packet.proto import TowerLevelEndNotify_pb2 as genshin_dot_packet_dot_proto_dot_TowerLevelEndNotify__pb2
from genshin.packet.proto import TrialAvatarFirstPassDungeonNotify_pb2 as genshin_dot_packet_dot_proto_dot_TrialAvatarFirstPassDungeonNotify__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/DungeonSettleNotify.proto\x1a=genshin/packet/proto/ChannelerSlabLoopDungeonResultInfo.proto\x1a\x30genshin/packet/proto/CrystalLinkSettleInfo.proto\x1a\x36genshin/packet/proto/DungeonSettleExhibitionInfo.proto\x1a;genshin/packet/proto/EffigyChallengeDungeonResultInfo.proto\x1a$genshin/packet/proto/ParamList.proto\x1a\x35genshin/packet/proto/RoguelikeDungeonSettleInfo.proto\x1a.genshin/packet/proto/StrengthenPointData.proto\x1a\x38genshin/packet/proto/SummerTimeV2DungeonSettleInfo.proto\x1a.genshin/packet/proto/TowerLevelEndNotify.proto\x1a<genshin/packet/proto/TrialAvatarFirstPassDungeonNotify.proto\"\x91\x08\n\x13\x44ungeonSettleNotify\x12S\n\x19strengthen_point_data_map\x18\x0e \x03(\x0b\x32\x30.DungeonSettleNotify.StrengthenPointDataMapEntry\x12\x12\n\nis_success\x18\x07 \x01(\x08\x12\x12\n\nclose_time\x18\x04 \x01(\r\x12\x1b\n\x13Unk2700_OMCCFBBDJMI\x18\x01 \x01(\r\x12\x39\n\x0bsettle_show\x18\x05 \x03(\x0b\x32$.DungeonSettleNotify.SettleShowEntry\x12:\n\x14\x65xhibition_info_list\x18\x08 \x03(\x0b\x32\x1c.DungeonSettleExhibitionInfo\x12\x16\n\x0e\x66\x61il_cond_list\x18\x0b \x03(\r\x12\x12\n\ndungeon_id\x18\r \x01(\r\x12\x0e\n\x06result\x18\n \x01(\r\x12\x37\n\x16tower_level_end_notify\x18\xdf\x02 \x01(\x0b\x32\x14.TowerLevelEndNotifyH\x00\x12U\n&trial_avatar_first_pass_dungeon_notify\x18\xfb\x04 \x01(\x0b\x32\".TrialAvatarFirstPassDungeonNotifyH\x00\x12X\n(channeller_slab_loop_dungeon_result_info\x18\xae\x05 \x01(\x0b\x32#.ChannelerSlabLoopDungeonResultInfoH\x00\x12R\n$effigy_challenge_dungeon_result_info\x18\xc8\x02 \x01(\x0b\x32!.EffigyChallengeDungeonResultInfoH\x00\x12\x45\n\x1droguelike_dungeon_settle_info\x18\xca\x0b \x01(\x0b\x32\x1b.RoguelikeDungeonSettleInfoH\x00\x12:\n\x18\x63rystal_link_settle_info\x18p \x01(\x0b\x32\x16.CrystalLinkSettleInfoH\x00\x12N\n#summer_time_v_2_dungeon_settle_info\x18\xda\x0e \x01(\x0b\x32\x1e.SummerTimeV2DungeonSettleInfoH\x00\x1aS\n\x1bStrengthenPointDataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.StrengthenPointData:\x02\x38\x01\x1a=\n\x0fSettleShowEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.ParamList:\x02\x38\x01\x42\x08\n\x06\x64\x65tailB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_DUNGEONSETTLENOTIFY = DESCRIPTOR.message_types_by_name['DungeonSettleNotify']
_DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY = _DUNGEONSETTLENOTIFY.nested_types_by_name['StrengthenPointDataMapEntry']
_DUNGEONSETTLENOTIFY_SETTLESHOWENTRY = _DUNGEONSETTLENOTIFY.nested_types_by_name['SettleShowEntry']
DungeonSettleNotify = _reflection.GeneratedProtocolMessageType('DungeonSettleNotify', (_message.Message,), {

  'StrengthenPointDataMapEntry' : _reflection.GeneratedProtocolMessageType('StrengthenPointDataMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY,
    '__module__' : 'genshin.packet.proto.DungeonSettleNotify_pb2'
    # @@protoc_insertion_point(class_scope:DungeonSettleNotify.StrengthenPointDataMapEntry)
    })
  ,

  'SettleShowEntry' : _reflection.GeneratedProtocolMessageType('SettleShowEntry', (_message.Message,), {
    'DESCRIPTOR' : _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY,
    '__module__' : 'genshin.packet.proto.DungeonSettleNotify_pb2'
    # @@protoc_insertion_point(class_scope:DungeonSettleNotify.SettleShowEntry)
    })
  ,
  'DESCRIPTOR' : _DUNGEONSETTLENOTIFY,
  '__module__' : 'genshin.packet.proto.DungeonSettleNotify_pb2'
  # @@protoc_insertion_point(class_scope:DungeonSettleNotify)
  })
_sym_db.RegisterMessage(DungeonSettleNotify)
_sym_db.RegisterMessage(DungeonSettleNotify.StrengthenPointDataMapEntry)
_sym_db.RegisterMessage(DungeonSettleNotify.SettleShowEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._options = None
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_options = b'8\001'
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._options = None
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_options = b'8\001'
  _DUNGEONSETTLENOTIFY._serialized_start=590
  _DUNGEONSETTLENOTIFY._serialized_end=1631
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_start=1475
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_end=1558
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_start=1560
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_end=1621
# @@protoc_insertion_point(module_scope)