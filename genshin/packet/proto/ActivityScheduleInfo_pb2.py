# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ActivityScheduleInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/ActivityScheduleInfo.proto\"w\n\x14\x41\x63tivityScheduleInfo\x12\x13\n\x0b\x61\x63tivity_id\x18\x0e \x01(\r\x12\x0f\n\x07is_open\x18\x02 \x01(\x08\x12\x13\n\x0bschedule_id\x18\r \x01(\r\x12\x12\n\nbegin_time\x18\n \x01(\r\x12\x10\n\x08\x65nd_time\x18\x01 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ACTIVITYSCHEDULEINFO = DESCRIPTOR.message_types_by_name['ActivityScheduleInfo']
ActivityScheduleInfo = _reflection.GeneratedProtocolMessageType('ActivityScheduleInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYSCHEDULEINFO,
  '__module__' : 'genshin.packet.proto.ActivityScheduleInfo_pb2'
  # @@protoc_insertion_point(class_scope:ActivityScheduleInfo)
  })
_sym_db.RegisterMessage(ActivityScheduleInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ACTIVITYSCHEDULEINFO._serialized_start=51
  _ACTIVITYSCHEDULEINFO._serialized_end=170
# @@protoc_insertion_point(module_scope)