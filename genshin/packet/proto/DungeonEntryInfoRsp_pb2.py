# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonEntryInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DungeonEntryInfo_pb2 as genshin_dot_packet_dot_proto_dot_DungeonEntryInfo__pb2
from genshin.packet.proto import Unk2800_MHCFAGCKGIB_pb2 as genshin_dot_packet_dot_proto_dot_Unk2800__MHCFAGCKGIB__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/DungeonEntryInfoRsp.proto\x1a+genshin/packet/proto/DungeonEntryInfo.proto\x1a.genshin/packet/proto/Unk2800_MHCFAGCKGIB.proto\"\xb8\x01\n\x13\x44ungeonEntryInfoRsp\x12-\n\x12\x64ungeon_entry_list\x18\x0c \x03(\x0b\x32\x11.DungeonEntryInfo\x12\x10\n\x08point_id\x18\x0f \x01(\r\x12\x31\n\x13Unk2800_JJFLDCLMEHD\x18\x04 \x03(\x0b\x32\x14.Unk2800_MHCFAGCKGIB\x12\x1c\n\x14recommend_dungeon_id\x18\x0e \x01(\r\x12\x0f\n\x07retcode\x18\x0b \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_DUNGEONENTRYINFORSP = DESCRIPTOR.message_types_by_name['DungeonEntryInfoRsp']
DungeonEntryInfoRsp = _reflection.GeneratedProtocolMessageType('DungeonEntryInfoRsp', (_message.Message,), {
  'DESCRIPTOR' : _DUNGEONENTRYINFORSP,
  '__module__' : 'genshin.packet.proto.DungeonEntryInfoRsp_pb2'
  # @@protoc_insertion_point(class_scope:DungeonEntryInfoRsp)
  })
_sym_db.RegisterMessage(DungeonEntryInfoRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _DUNGEONENTRYINFORSP._serialized_start=144
  _DUNGEONENTRYINFORSP._serialized_end=328
# @@protoc_insertion_point(module_scope)