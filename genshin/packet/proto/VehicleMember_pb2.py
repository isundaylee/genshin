# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/VehicleMember.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/VehicleMember.proto\">\n\rVehicleMember\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x13\n\x0b\x61vatar_guid\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_VEHICLEMEMBER = DESCRIPTOR.message_types_by_name['VehicleMember']
VehicleMember = _reflection.GeneratedProtocolMessageType('VehicleMember', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLEMEMBER,
  '__module__' : 'genshin.packet.proto.VehicleMember_pb2'
  # @@protoc_insertion_point(class_scope:VehicleMember)
  })
_sym_db.RegisterMessage(VehicleMember)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _VEHICLEMEMBER._serialized_start=44
  _VEHICLEMEMBER._serialized_end=106
# @@protoc_insertion_point(module_scope)
