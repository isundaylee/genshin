# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuestProgressUpdateNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/QuestProgressUpdateNotify.proto\"g\n\x19QuestProgressUpdateNotify\x12\x10\n\x08quest_id\x18\x0c \x01(\r\x12\x1a\n\x12\x66\x61il_progress_list\x18\x06 \x03(\r\x12\x1c\n\x14\x66inish_progress_list\x18\r \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_QUESTPROGRESSUPDATENOTIFY = DESCRIPTOR.message_types_by_name['QuestProgressUpdateNotify']
QuestProgressUpdateNotify = _reflection.GeneratedProtocolMessageType('QuestProgressUpdateNotify', (_message.Message,), {
  'DESCRIPTOR' : _QUESTPROGRESSUPDATENOTIFY,
  '__module__' : 'genshin.packet.proto.QuestProgressUpdateNotify_pb2'
  # @@protoc_insertion_point(class_scope:QuestProgressUpdateNotify)
  })
_sym_db.RegisterMessage(QuestProgressUpdateNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _QUESTPROGRESSUPDATENOTIFY._serialized_start=56
  _QUESTPROGRESSUPDATENOTIFY._serialized_end=159
# @@protoc_insertion_point(module_scope)
