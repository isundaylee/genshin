# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneGadgetInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilityGadgetInfo__pb2
from genshin.packet.proto import BlossomChestInfo_pb2 as genshin_dot_packet_dot_proto_dot_BlossomChestInfo__pb2
from genshin.packet.proto import BossChestInfo_pb2 as genshin_dot_packet_dot_proto_dot_BossChestInfo__pb2
from genshin.packet.proto import ClientGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_ClientGadgetInfo__pb2
from genshin.packet.proto import CustomGadgetTreeInfo_pb2 as genshin_dot_packet_dot_proto_dot_CustomGadgetTreeInfo__pb2
from genshin.packet.proto import EchoShellInfo_pb2 as genshin_dot_packet_dot_proto_dot_EchoShellInfo__pb2
from genshin.packet.proto import FishPoolInfo_pb2 as genshin_dot_packet_dot_proto_dot_FishPoolInfo__pb2
from genshin.packet.proto import FoundationInfo_pb2 as genshin_dot_packet_dot_proto_dot_FoundationInfo__pb2
from genshin.packet.proto import GadgetBornType_pb2 as genshin_dot_packet_dot_proto_dot_GadgetBornType__pb2
from genshin.packet.proto import GadgetGeneralRewardInfo_pb2 as genshin_dot_packet_dot_proto_dot_GadgetGeneralRewardInfo__pb2
from genshin.packet.proto import GadgetPlayInfo_pb2 as genshin_dot_packet_dot_proto_dot_GadgetPlayInfo__pb2
from genshin.packet.proto import GatherGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_GatherGadgetInfo__pb2
from genshin.packet.proto import Item_pb2 as genshin_dot_packet_dot_proto_dot_Item__pb2
from genshin.packet.proto import MpPlayRewardInfo_pb2 as genshin_dot_packet_dot_proto_dot_MpPlayRewardInfo__pb2
from genshin.packet.proto import OfferingInfo_pb2 as genshin_dot_packet_dot_proto_dot_OfferingInfo__pb2
from genshin.packet.proto import PlatformInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlatformInfo__pb2
from genshin.packet.proto import RoguelikeGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_RoguelikeGadgetInfo__pb2
from genshin.packet.proto import ScreenInfo_pb2 as genshin_dot_packet_dot_proto_dot_ScreenInfo__pb2
from genshin.packet.proto import StatueGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_StatueGadgetInfo__pb2
from genshin.packet.proto import Unk2800_FHMOLALLEEN_pb2 as genshin_dot_packet_dot_proto_dot_Unk2800__FHMOLALLEEN__pb2
from genshin.packet.proto import VehicleInfo_pb2 as genshin_dot_packet_dot_proto_dot_VehicleInfo__pb2
from genshin.packet.proto import WeatherInfo_pb2 as genshin_dot_packet_dot_proto_dot_WeatherInfo__pb2
from genshin.packet.proto import WorktopInfo_pb2 as genshin_dot_packet_dot_proto_dot_WorktopInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SceneGadgetInfo.proto\x1a,genshin/packet/proto/AbilityGadgetInfo.proto\x1a+genshin/packet/proto/BlossomChestInfo.proto\x1a(genshin/packet/proto/BossChestInfo.proto\x1a+genshin/packet/proto/ClientGadgetInfo.proto\x1a/genshin/packet/proto/CustomGadgetTreeInfo.proto\x1a(genshin/packet/proto/EchoShellInfo.proto\x1a\'genshin/packet/proto/FishPoolInfo.proto\x1a)genshin/packet/proto/FoundationInfo.proto\x1a)genshin/packet/proto/GadgetBornType.proto\x1a\x32genshin/packet/proto/GadgetGeneralRewardInfo.proto\x1a)genshin/packet/proto/GadgetPlayInfo.proto\x1a+genshin/packet/proto/GatherGadgetInfo.proto\x1a\x1fgenshin/packet/proto/Item.proto\x1a+genshin/packet/proto/MpPlayRewardInfo.proto\x1a\'genshin/packet/proto/OfferingInfo.proto\x1a\'genshin/packet/proto/PlatformInfo.proto\x1a.genshin/packet/proto/RoguelikeGadgetInfo.proto\x1a%genshin/packet/proto/ScreenInfo.proto\x1a+genshin/packet/proto/StatueGadgetInfo.proto\x1a.genshin/packet/proto/Unk2800_FHMOLALLEEN.proto\x1a&genshin/packet/proto/VehicleInfo.proto\x1a&genshin/packet/proto/WeatherInfo.proto\x1a&genshin/packet/proto/WorktopInfo.proto\"\xbb\n\n\x0fSceneGadgetInfo\x12\x11\n\tgadget_id\x18\x01 \x01(\r\x12\x10\n\x08group_id\x18\x02 \x01(\r\x12\x11\n\tconfig_id\x18\x03 \x01(\r\x12\x17\n\x0fowner_entity_id\x18\x04 \x01(\r\x12\"\n\tborn_type\x18\x05 \x01(\x0e\x32\x0f.GadgetBornType\x12\x14\n\x0cgadget_state\x18\x06 \x01(\r\x12\x13\n\x0bgadget_type\x18\x07 \x01(\r\x12\x18\n\x10is_show_cutscene\x18\x08 \x01(\x08\x12\x19\n\x11\x61uthority_peer_id\x18\t \x01(\r\x12\x1a\n\x12is_enable_interact\x18\n \x01(\x08\x12\x13\n\x0binteract_id\x18\x0b \x01(\r\x12\x11\n\tmark_flag\x18\x15 \x01(\r\x12\x1c\n\x14prop_owner_entity_id\x18\x16 \x01(\r\x12\x1f\n\x08platform\x18\x17 \x01(\x0b\x32\r.PlatformInfo\x12\x19\n\x11interact_uid_list\x18\x18 \x03(\r\x12\x10\n\x08\x64raft_id\x18\x19 \x01(\r\x12\x19\n\x11gadget_talk_state\x18\x1a \x01(\r\x12\"\n\tplay_info\x18\x64 \x01(\x0b\x32\x0f.GadgetPlayInfo\x12\x1c\n\x0btrifle_item\x18\x0c \x01(\x0b\x32\x05.ItemH\x00\x12*\n\rgather_gadget\x18\r \x01(\x0b\x32\x11.GatherGadgetInfoH\x00\x12\x1f\n\x07worktop\x18\x0e \x01(\x0b\x32\x0c.WorktopInfoH\x00\x12*\n\rclient_gadget\x18\x0f \x01(\x0b\x32\x11.ClientGadgetInfoH\x00\x12\x1f\n\x07weather\x18\x11 \x01(\x0b\x32\x0c.WeatherInfoH\x00\x12,\n\x0e\x61\x62ility_gadget\x18\x12 \x01(\x0b\x32\x12.AbilityGadgetInfoH\x00\x12*\n\rstatue_gadget\x18\x13 \x01(\x0b\x32\x11.StatueGadgetInfoH\x00\x12$\n\nboss_chest\x18\x14 \x01(\x0b\x32\x0e.BossChestInfoH\x00\x12*\n\rblossom_chest\x18) \x01(\x0b\x32\x11.BlossomChestInfoH\x00\x12+\n\x0emp_play_reward\x18* \x01(\x0b\x32\x11.MpPlayRewardInfoH\x00\x12\x32\n\x0egeneral_reward\x18+ \x01(\x0b\x32\x18.GadgetGeneralRewardInfoH\x00\x12&\n\roffering_info\x18, \x01(\x0b\x32\r.OfferingInfoH\x00\x12*\n\x0f\x66oundation_info\x18- \x01(\x0b\x32\x0f.FoundationInfoH\x00\x12$\n\x0cvehicle_info\x18. \x01(\x0b\x32\x0c.VehicleInfoH\x00\x12$\n\nshell_info\x18/ \x01(\x0b\x32\x0e.EchoShellInfoH\x00\x12\"\n\x0bscreen_info\x18\x30 \x01(\x0b\x32\x0b.ScreenInfoH\x00\x12\'\n\x0e\x66ish_pool_info\x18; \x01(\x0b\x32\r.FishPoolInfoH\x00\x12\x38\n\x17\x63ustom_gadget_tree_info\x18< \x01(\x0b\x32\x15.CustomGadgetTreeInfoH\x00\x12\x35\n\x15roguelike_gadget_info\x18= \x01(\x0b\x32\x14.RoguelikeGadgetInfoH\x00\x12\x36\n\x16night_crow_gadget_info\x18> \x01(\x0b\x32\x14.Unk2800_FHMOLALLEENH\x00\x42\t\n\x07\x63ontentB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SCENEGADGETINFO = DESCRIPTOR.message_types_by_name['SceneGadgetInfo']
SceneGadgetInfo = _reflection.GeneratedProtocolMessageType('SceneGadgetInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENEGADGETINFO,
  '__module__' : 'genshin.packet.proto.SceneGadgetInfo_pb2'
  # @@protoc_insertion_point(class_scope:SceneGadgetInfo)
  })
_sym_db.RegisterMessage(SceneGadgetInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SCENEGADGETINFO._serialized_start=1043
  _SCENEGADGETINFO._serialized_end=2382
# @@protoc_insertion_point(module_scope)
