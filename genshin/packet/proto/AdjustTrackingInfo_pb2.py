# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AdjustTrackingInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/AdjustTrackingInfo.proto\"}\n\x12\x41\x64justTrackingInfo\x12\x13\n\x0b\x65vent_token\x18\t \x01(\t\x12\x0c\n\x04\x61\x64id\x18\x04 \x01(\t\x12\x0c\n\x04idfa\x18\x02 \x01(\t\x12\x11\n\tapp_token\x18\x0e \x01(\t\x12\x10\n\x08gps_adid\x18\x03 \x01(\t\x12\x11\n\tfire_adid\x18\r \x01(\tB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ADJUSTTRACKINGINFO = DESCRIPTOR.message_types_by_name['AdjustTrackingInfo']
AdjustTrackingInfo = _reflection.GeneratedProtocolMessageType('AdjustTrackingInfo', (_message.Message,), {
  'DESCRIPTOR' : _ADJUSTTRACKINGINFO,
  '__module__' : 'genshin.packet.proto.AdjustTrackingInfo_pb2'
  # @@protoc_insertion_point(class_scope:AdjustTrackingInfo)
  })
_sym_db.RegisterMessage(AdjustTrackingInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ADJUSTTRACKINGINFO._serialized_start=49
  _ADJUSTTRACKINGINFO._serialized_end=174
# @@protoc_insertion_point(module_scope)
