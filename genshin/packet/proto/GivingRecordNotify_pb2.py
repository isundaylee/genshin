# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GivingRecordNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import GivingRecord_pb2 as genshin_dot_packet_dot_proto_dot_GivingRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/GivingRecordNotify.proto\x1a\'genshin/packet/proto/GivingRecord.proto\"?\n\x12GivingRecordNotify\x12)\n\x12giving_record_list\x18\x0e \x03(\x0b\x32\r.GivingRecordB\x16\n\x14org.sorapointa.protob\x06proto3')



_GIVINGRECORDNOTIFY = DESCRIPTOR.message_types_by_name['GivingRecordNotify']
GivingRecordNotify = _reflection.GeneratedProtocolMessageType('GivingRecordNotify', (_message.Message,), {
  'DESCRIPTOR' : _GIVINGRECORDNOTIFY,
  '__module__' : 'genshin.packet.proto.GivingRecordNotify_pb2'
  # @@protoc_insertion_point(class_scope:GivingRecordNotify)
  })
_sym_db.RegisterMessage(GivingRecordNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GIVINGRECORDNOTIFY._serialized_start=90
  _GIVINGRECORDNOTIFY._serialized_end=153
# @@protoc_insertion_point(module_scope)
