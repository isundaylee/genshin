# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientLogHead.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/ClientLogHead.proto\"\xb4\x02\n\rClientLogHead\x12\x12\n\nevent_time\x18\x01 \x01(\t\x12\x19\n\x11log_serial_number\x18\x02 \x01(\t\x12\x11\n\taction_id\x18\x03 \x01(\r\x12\x13\n\x0b\x61\x63tion_name\x18\x04 \x01(\t\x12\x11\n\tupload_ip\x18\x05 \x01(\t\x12\x12\n\nproduct_id\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\t\x12\x13\n\x0bregion_name\x18\x08 \x01(\t\x12\x14\n\x0cgame_version\x18\t \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\n \x01(\t\x12\x13\n\x0b\x64\x65vice_uuid\x18\x0b \x01(\t\x12\x10\n\x08mac_addr\x18\x0c \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_name\x18\r \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_uuid\x18\x0e \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTLOGHEAD = DESCRIPTOR.message_types_by_name['ClientLogHead']
ClientLogHead = _reflection.GeneratedProtocolMessageType('ClientLogHead', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLOGHEAD,
  '__module__' : 'genshin.packet.proto.ClientLogHead_pb2'
  # @@protoc_insertion_point(class_scope:ClientLogHead)
  })
_sym_db.RegisterMessage(ClientLogHead)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTLOGHEAD._serialized_start=45
  _CLIENTLOGHEAD._serialized_end=353
# @@protoc_insertion_point(module_scope)
