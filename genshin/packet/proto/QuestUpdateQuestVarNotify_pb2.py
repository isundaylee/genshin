# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuestUpdateQuestVarNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/QuestUpdateQuestVarNotify.proto\"e\n\x19QuestUpdateQuestVarNotify\x12\x11\n\tquest_var\x18\x01 \x03(\x05\x12\x17\n\x0fparent_quest_id\x18\x0c \x01(\r\x12\x1c\n\x14parent_quest_var_seq\x18\x08 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_QUESTUPDATEQUESTVARNOTIFY = DESCRIPTOR.message_types_by_name['QuestUpdateQuestVarNotify']
QuestUpdateQuestVarNotify = _reflection.GeneratedProtocolMessageType('QuestUpdateQuestVarNotify', (_message.Message,), {
  'DESCRIPTOR' : _QUESTUPDATEQUESTVARNOTIFY,
  '__module__' : 'genshin.packet.proto.QuestUpdateQuestVarNotify_pb2'
  # @@protoc_insertion_point(class_scope:QuestUpdateQuestVarNotify)
  })
_sym_db.RegisterMessage(QuestUpdateQuestVarNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _QUESTUPDATEQUESTVARNOTIFY._serialized_start=56
  _QUESTUPDATEQUESTVARNOTIFY._serialized_end=157
# @@protoc_insertion_point(module_scope)
