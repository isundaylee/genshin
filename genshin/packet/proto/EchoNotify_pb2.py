# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EchoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/EchoNotify.proto\"-\n\nEchoNotify\x12\x0e\n\x06seq_id\x18\x04 \x01(\r\x12\x0f\n\x07\x63ontent\x18\t \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_ECHONOTIFY = DESCRIPTOR.message_types_by_name['EchoNotify']
EchoNotify = _reflection.GeneratedProtocolMessageType('EchoNotify', (_message.Message,), {
  'DESCRIPTOR' : _ECHONOTIFY,
  '__module__' : 'genshin.packet.proto.EchoNotify_pb2'
  # @@protoc_insertion_point(class_scope:EchoNotify)
  })
_sym_db.RegisterMessage(EchoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ECHONOTIFY._serialized_start=41
  _ECHONOTIFY._serialized_end=86
# @@protoc_insertion_point(module_scope)