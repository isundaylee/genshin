# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuestDestroyNpcReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/QuestDestroyNpcReq.proto\"=\n\x12QuestDestroyNpcReq\x12\x0e\n\x06npc_id\x18\x01 \x01(\r\x12\x17\n\x0fparent_quest_id\x18\x0c \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_QUESTDESTROYNPCREQ = DESCRIPTOR.message_types_by_name['QuestDestroyNpcReq']
QuestDestroyNpcReq = _reflection.GeneratedProtocolMessageType('QuestDestroyNpcReq', (_message.Message,), {
  'DESCRIPTOR' : _QUESTDESTROYNPCREQ,
  '__module__' : 'genshin.packet.proto.QuestDestroyNpcReq_pb2'
  # @@protoc_insertion_point(class_scope:QuestDestroyNpcReq)
  })
_sym_db.RegisterMessage(QuestDestroyNpcReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _QUESTDESTROYNPCREQ._serialized_start=49
  _QUESTDESTROYNPCREQ._serialized_end=110
# @@protoc_insertion_point(module_scope)