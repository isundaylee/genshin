# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ReunionMissionInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ReunionWatcherInfo_pb2 as genshin_dot_packet_dot_proto_dot_ReunionWatcherInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/ReunionMissionInfo.proto\x1a-genshin/packet/proto/ReunionWatcherInfo.proto\"\x80\x02\n\x12ReunionMissionInfo\x12\x31\n\x14\x63ur_day_watcher_list\x18\x03 \x03(\x0b\x32\x13.ReunionWatcherInfo\x12\x11\n\tcur_score\x18\x0b \x01(\r\x12\x17\n\x0fis_taken_reward\x18\x08 \x01(\x08\x12\x1c\n\x14is_taken_reward_list\x18\x06 \x03(\x08\x12\x19\n\x11next_refresh_time\x18\x05 \x01(\r\x12\x13\n\x0bis_finished\x18\t \x01(\x08\x12\x12\n\nmission_id\x18\x0c \x01(\r\x12)\n\x0cwatcher_list\x18\x02 \x03(\x0b\x32\x13.ReunionWatcherInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_REUNIONMISSIONINFO = DESCRIPTOR.message_types_by_name['ReunionMissionInfo']
ReunionMissionInfo = _reflection.GeneratedProtocolMessageType('ReunionMissionInfo', (_message.Message,), {
  'DESCRIPTOR' : _REUNIONMISSIONINFO,
  '__module__' : 'genshin.packet.proto.ReunionMissionInfo_pb2'
  # @@protoc_insertion_point(class_scope:ReunionMissionInfo)
  })
_sym_db.RegisterMessage(ReunionMissionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _REUNIONMISSIONINFO._serialized_start=97
  _REUNIONMISSIONINFO._serialized_end=353
# @@protoc_insertion_point(module_scope)
