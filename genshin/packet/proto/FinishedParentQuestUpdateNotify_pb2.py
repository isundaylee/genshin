# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FinishedParentQuestUpdateNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ParentQuest_pb2 as genshin_dot_packet_dot_proto_dot_ParentQuest__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:genshin/packet/proto/FinishedParentQuestUpdateNotify.proto\x1a&genshin/packet/proto/ParentQuest.proto\"J\n\x1f\x46inishedParentQuestUpdateNotify\x12\'\n\x11parent_quest_list\x18\t \x03(\x0b\x32\x0c.ParentQuestB\x16\n\x14org.sorapointa.protob\x06proto3')



_FINISHEDPARENTQUESTUPDATENOTIFY = DESCRIPTOR.message_types_by_name['FinishedParentQuestUpdateNotify']
FinishedParentQuestUpdateNotify = _reflection.GeneratedProtocolMessageType('FinishedParentQuestUpdateNotify', (_message.Message,), {
  'DESCRIPTOR' : _FINISHEDPARENTQUESTUPDATENOTIFY,
  '__module__' : 'genshin.packet.proto.FinishedParentQuestUpdateNotify_pb2'
  # @@protoc_insertion_point(class_scope:FinishedParentQuestUpdateNotify)
  })
_sym_db.RegisterMessage(FinishedParentQuestUpdateNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FINISHEDPARENTQUESTUPDATENOTIFY._serialized_start=102
  _FINISHEDPARENTQUESTUPDATENOTIFY._serialized_end=176
# @@protoc_insertion_point(module_scope)
