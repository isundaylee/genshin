# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DebugNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/DebugNotify.proto\"}\n\x0b\x44\x65\x62ugNotify\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x07retcode\x18\x03 \x01(\x0e\x32\x14.DebugNotify.Retcode\"-\n\x07Retcode\x12\x10\n\x0cRETCODE_SUCC\x10\x00\x12\x10\n\x0cRETCODE_FAIL\x10\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_DEBUGNOTIFY = DESCRIPTOR.message_types_by_name['DebugNotify']
_DEBUGNOTIFY_RETCODE = _DEBUGNOTIFY.enum_types_by_name['Retcode']
DebugNotify = _reflection.GeneratedProtocolMessageType('DebugNotify', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGNOTIFY,
  '__module__' : 'genshin.packet.proto.DebugNotify_pb2'
  # @@protoc_insertion_point(class_scope:DebugNotify)
  })
_sym_db.RegisterMessage(DebugNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DEBUGNOTIFY._serialized_start=42
  _DEBUGNOTIFY._serialized_end=167
  _DEBUGNOTIFY_RETCODE._serialized_start=122
  _DEBUGNOTIFY_RETCODE._serialized_end=167
# @@protoc_insertion_point(module_scope)
