# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BattlePassCurScheduleUpdateNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassSchedule_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassSchedule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<genshin/packet/proto/BattlePassCurScheduleUpdateNotify.proto\x1a-genshin/packet/proto/BattlePassSchedule.proto\"i\n!BattlePassCurScheduleUpdateNotify\x12\x19\n\x11have_cur_schedule\x18\x0b \x01(\x08\x12)\n\x0c\x63ur_schedule\x18\x01 \x01(\x0b\x32\x13.BattlePassScheduleB\x16\n\x14org.sorapointa.protob\x06proto3')



_BATTLEPASSCURSCHEDULEUPDATENOTIFY = DESCRIPTOR.message_types_by_name['BattlePassCurScheduleUpdateNotify']
BattlePassCurScheduleUpdateNotify = _reflection.GeneratedProtocolMessageType('BattlePassCurScheduleUpdateNotify', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPASSCURSCHEDULEUPDATENOTIFY,
  '__module__' : 'genshin.packet.proto.BattlePassCurScheduleUpdateNotify_pb2'
  # @@protoc_insertion_point(class_scope:BattlePassCurScheduleUpdateNotify)
  })
_sym_db.RegisterMessage(BattlePassCurScheduleUpdateNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BATTLEPASSCURSCHEDULEUPDATENOTIFY._serialized_start=111
  _BATTLEPASSCURSCHEDULEUPDATENOTIFY._serialized_end=216
# @@protoc_insertion_point(module_scope)
