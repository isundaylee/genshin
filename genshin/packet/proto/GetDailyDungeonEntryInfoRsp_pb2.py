# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetDailyDungeonEntryInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DailyDungeonEntryInfo_pb2 as genshin_dot_packet_dot_proto_dot_DailyDungeonEntryInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/GetDailyDungeonEntryInfoRsp.proto\x1a\x30genshin/packet/proto/DailyDungeonEntryInfo.proto\"g\n\x1bGetDailyDungeonEntryInfoRsp\x12\x37\n\x17\x64\x61ily_dungeon_info_list\x18\x02 \x03(\x0b\x32\x16.DailyDungeonEntryInfo\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GETDAILYDUNGEONENTRYINFORSP = DESCRIPTOR.message_types_by_name['GetDailyDungeonEntryInfoRsp']
GetDailyDungeonEntryInfoRsp = _reflection.GeneratedProtocolMessageType('GetDailyDungeonEntryInfoRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETDAILYDUNGEONENTRYINFORSP,
  '__module__' : 'genshin.packet.proto.GetDailyDungeonEntryInfoRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetDailyDungeonEntryInfoRsp)
  })
_sym_db.RegisterMessage(GetDailyDungeonEntryInfoRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETDAILYDUNGEONENTRYINFORSP._serialized_start=108
  _GETDAILYDUNGEONENTRYINFORSP._serialized_end=211
# @@protoc_insertion_point(module_scope)
