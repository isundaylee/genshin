# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuestUpdateQuestVarRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/QuestUpdateQuestVarRsp.proto\"r\n\x16QuestUpdateQuestVarRsp\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12\x1c\n\x14parent_quest_var_seq\x18\x02 \x01(\r\x12\x17\n\x0fparent_quest_id\x18\x08 \x01(\r\x12\x10\n\x08quest_id\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_QUESTUPDATEQUESTVARRSP = DESCRIPTOR.message_types_by_name['QuestUpdateQuestVarRsp']
QuestUpdateQuestVarRsp = _reflection.GeneratedProtocolMessageType('QuestUpdateQuestVarRsp', (_message.Message,), {
  'DESCRIPTOR' : _QUESTUPDATEQUESTVARRSP,
  '__module__' : 'genshin.packet.proto.QuestUpdateQuestVarRsp_pb2'
  # @@protoc_insertion_point(class_scope:QuestUpdateQuestVarRsp)
  })
_sym_db.RegisterMessage(QuestUpdateQuestVarRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _QUESTUPDATEQUESTVARRSP._serialized_start=53
  _QUESTUPDATEQUESTVARRSP._serialized_end=167
# @@protoc_insertion_point(module_scope)