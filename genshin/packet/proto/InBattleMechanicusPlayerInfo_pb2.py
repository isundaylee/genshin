# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/InBattleMechanicusPlayerInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import InBattleMechanicusBuildingInfo_pb2 as genshin_dot_packet_dot_proto_dot_InBattleMechanicusBuildingInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/InBattleMechanicusPlayerInfo.proto\x1a\x39genshin/packet/proto/InBattleMechanicusBuildingInfo.proto\"\xad\x01\n\x1cInBattleMechanicusPlayerInfo\x12\x14\n\x0cpick_card_id\x18\x05 \x01(\r\x12\x0b\n\x03uid\x18\x0e \x01(\r\x12\x36\n\rbuilding_list\x18\x04 \x03(\x0b\x32\x1f.InBattleMechanicusBuildingInfo\x12\x19\n\x11is_card_confirmed\x18\r \x01(\x08\x12\x17\n\x0f\x62uilding_points\x18\x03 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_INBATTLEMECHANICUSPLAYERINFO = DESCRIPTOR.message_types_by_name['InBattleMechanicusPlayerInfo']
InBattleMechanicusPlayerInfo = _reflection.GeneratedProtocolMessageType('InBattleMechanicusPlayerInfo', (_message.Message,), {
  'DESCRIPTOR' : _INBATTLEMECHANICUSPLAYERINFO,
  '__module__' : 'genshin.packet.proto.InBattleMechanicusPlayerInfo_pb2'
  # @@protoc_insertion_point(class_scope:InBattleMechanicusPlayerInfo)
  })
_sym_db.RegisterMessage(InBattleMechanicusPlayerInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _INBATTLEMECHANICUSPLAYERINFO._serialized_start=119
  _INBATTLEMECHANICUSPLAYERINFO._serialized_end=292
# @@protoc_insertion_point(module_scope)
