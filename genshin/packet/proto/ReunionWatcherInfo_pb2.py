# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ReunionWatcherInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/ReunionWatcherInfo.proto\"\x8b\x01\n\x12ReunionWatcherInfo\x12\x1a\n\x12reward_unlock_time\x18\x0c \x01(\r\x12\x12\n\nwatcher_id\x18\x03 \x01(\r\x12\x16\n\x0etotal_progress\x18\x04 \x01(\r\x12\x14\n\x0c\x63ur_progress\x18\x0b \x01(\r\x12\x17\n\x0fis_taken_reward\x18\x0e \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_REUNIONWATCHERINFO = DESCRIPTOR.message_types_by_name['ReunionWatcherInfo']
ReunionWatcherInfo = _reflection.GeneratedProtocolMessageType('ReunionWatcherInfo', (_message.Message,), {
  'DESCRIPTOR' : _REUNIONWATCHERINFO,
  '__module__' : 'genshin.packet.proto.ReunionWatcherInfo_pb2'
  # @@protoc_insertion_point(class_scope:ReunionWatcherInfo)
  })
_sym_db.RegisterMessage(ReunionWatcherInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _REUNIONWATCHERINFO._serialized_start=50
  _REUNIONWATCHERINFO._serialized_end=189
# @@protoc_insertion_point(module_scope)