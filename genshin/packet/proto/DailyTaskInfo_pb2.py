# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DailyTaskInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/DailyTaskInfo.proto\"y\n\rDailyTaskInfo\x12\x11\n\treward_id\x18\x03 \x01(\r\x12\x10\n\x08progress\x18\r \x01(\r\x12\x17\n\x0f\x66inish_progress\x18\n \x01(\r\x12\x15\n\rdaily_task_id\x18\x04 \x01(\r\x12\x13\n\x0bis_finished\x18\x0e \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_DAILYTASKINFO = DESCRIPTOR.message_types_by_name['DailyTaskInfo']
DailyTaskInfo = _reflection.GeneratedProtocolMessageType('DailyTaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _DAILYTASKINFO,
  '__module__' : 'genshin.packet.proto.DailyTaskInfo_pb2'
  # @@protoc_insertion_point(class_scope:DailyTaskInfo)
  })
_sym_db.RegisterMessage(DailyTaskInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DAILYTASKINFO._serialized_start=44
  _DAILYTASKINFO._serialized_end=165
# @@protoc_insertion_point(module_scope)
