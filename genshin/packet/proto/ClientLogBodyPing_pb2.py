# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientLogBodyPing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/ClientLogBodyPing.proto\"\xa9\x01\n\x11\x43lientLogBodyPing\x12\n\n\x02xg\x18\x01 \x01(\t\x12\x14\n\x0csignal_level\x18\x02 \x01(\r\x12\x0c\n\x04ping\x18\x03 \x01(\r\x12\x12\n\nservertype\x18\x04 \x01(\t\x12\x10\n\x08serverip\x18\x05 \x01(\t\x12\x12\n\nserverport\x18\x06 \x01(\t\x12\x0e\n\x06pcount\x18\x07 \x01(\r\x12\r\n\x05plost\x18\x08 \x01(\r\x12\x0b\n\x03\x64ns\x18\t \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTLOGBODYPING = DESCRIPTOR.message_types_by_name['ClientLogBodyPing']
ClientLogBodyPing = _reflection.GeneratedProtocolMessageType('ClientLogBodyPing', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLOGBODYPING,
  '__module__' : 'genshin.packet.proto.ClientLogBodyPing_pb2'
  # @@protoc_insertion_point(class_scope:ClientLogBodyPing)
  })
_sym_db.RegisterMessage(ClientLogBodyPing)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTLOGBODYPING._serialized_start=49
  _CLIENTLOGBODYPING._serialized_end=218
# @@protoc_insertion_point(module_scope)
