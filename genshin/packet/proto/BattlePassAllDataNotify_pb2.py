# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BattlePassAllDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassMission_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassMission__pb2
from genshin.packet.proto import BattlePassSchedule_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassSchedule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/BattlePassAllDataNotify.proto\x1a,genshin/packet/proto/BattlePassMission.proto\x1a-genshin/packet/proto/BattlePassSchedule.proto\"\x89\x01\n\x17\x42\x61ttlePassAllDataNotify\x12\x19\n\x11have_cur_schedule\x18\x02 \x01(\x08\x12)\n\x0c\x63ur_schedule\x18\x01 \x01(\x0b\x32\x13.BattlePassSchedule\x12(\n\x0cmission_list\x18\x04 \x03(\x0b\x32\x12.BattlePassMissionB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_BATTLEPASSALLDATANOTIFY = DESCRIPTOR.message_types_by_name['BattlePassAllDataNotify']
BattlePassAllDataNotify = _reflection.GeneratedProtocolMessageType('BattlePassAllDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPASSALLDATANOTIFY,
  '__module__' : 'genshin.packet.proto.BattlePassAllDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:BattlePassAllDataNotify)
  })
_sym_db.RegisterMessage(BattlePassAllDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _BATTLEPASSALLDATANOTIFY._serialized_start=148
  _BATTLEPASSALLDATANOTIFY._serialized_end=285
# @@protoc_insertion_point(module_scope)
