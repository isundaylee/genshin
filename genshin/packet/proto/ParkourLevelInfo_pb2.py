# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ParkourLevelInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/ParkourLevelInfo.proto\x1a!genshin/packet/proto/Vector.proto\"a\n\x10ParkourLevelInfo\x12\x13\n\x0b\x62\x65st_record\x18\x0c \x01(\r\x12\x0f\n\x07is_open\x18\t \x01(\x08\x12\x11\n\topen_time\x18\x07 \x01(\r\x12\x14\n\x03pos\x18\x02 \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_PARKOURLEVELINFO = DESCRIPTOR.message_types_by_name['ParkourLevelInfo']
ParkourLevelInfo = _reflection.GeneratedProtocolMessageType('ParkourLevelInfo', (_message.Message,), {
  'DESCRIPTOR' : _PARKOURLEVELINFO,
  '__module__' : 'genshin.packet.proto.ParkourLevelInfo_pb2'
  # @@protoc_insertion_point(class_scope:ParkourLevelInfo)
  })
_sym_db.RegisterMessage(ParkourLevelInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PARKOURLEVELINFO._serialized_start=82
  _PARKOURLEVELINFO._serialized_end=179
# @@protoc_insertion_point(module_scope)
