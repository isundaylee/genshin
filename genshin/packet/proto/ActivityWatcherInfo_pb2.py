# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ActivityWatcherInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/ActivityWatcherInfo.proto\"p\n\x13\x41\x63tivityWatcherInfo\x12\x17\n\x0fis_taken_reward\x18\x08 \x01(\x08\x12\x14\n\x0c\x63ur_progress\x18\x02 \x01(\r\x12\x16\n\x0etotal_progress\x18\x04 \x01(\r\x12\x12\n\nwatcher_id\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_ACTIVITYWATCHERINFO = DESCRIPTOR.message_types_by_name['ActivityWatcherInfo']
ActivityWatcherInfo = _reflection.GeneratedProtocolMessageType('ActivityWatcherInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYWATCHERINFO,
  '__module__' : 'genshin.packet.proto.ActivityWatcherInfo_pb2'
  # @@protoc_insertion_point(class_scope:ActivityWatcherInfo)
  })
_sym_db.RegisterMessage(ActivityWatcherInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ACTIVITYWATCHERINFO._serialized_start=50
  _ACTIVITYWATCHERINFO._serialized_end=162
# @@protoc_insertion_point(module_scope)
