# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TrackingIOInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/TrackingIOInfo.proto\"\x92\x01\n\x0eTrackingIOInfo\x12\x14\n\x0crydevicetype\x18\x0b \x01(\t\x12\x0b\n\x03mac\x18\x06 \x01(\t\x12\x10\n\x08\x64\x65viceid\x18\t \x01(\t\x12\x11\n\tclient_tz\x18\x05 \x01(\t\x12\x14\n\x0c\x63urrent_caid\x18\x07 \x01(\t\x12\x13\n\x0b\x63\x61\x63hed_caid\x18\x0f \x01(\t\x12\r\n\x05\x61ppid\x18\x01 \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_TRACKINGIOINFO = DESCRIPTOR.message_types_by_name['TrackingIOInfo']
TrackingIOInfo = _reflection.GeneratedProtocolMessageType('TrackingIOInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRACKINGIOINFO,
  '__module__' : 'genshin.packet.proto.TrackingIOInfo_pb2'
  # @@protoc_insertion_point(class_scope:TrackingIOInfo)
  })
_sym_db.RegisterMessage(TrackingIOInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TRACKINGIOINFO._serialized_start=46
  _TRACKINGIOINFO._serialized_end=192
# @@protoc_insertion_point(module_scope)
