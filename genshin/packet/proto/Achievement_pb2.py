# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Achievement.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/Achievement.proto\"\xe9\x01\n\x0b\x41\x63hievement\x12\x18\n\x10\x66inish_timestamp\x18\x0b \x01(\r\x12#\n\x06status\x18\r \x01(\x0e\x32\x13.Achievement.Status\x12\x14\n\x0c\x63ur_progress\x18\x0c \x01(\r\x12\n\n\x02id\x18\x0e \x01(\r\x12\x16\n\x0etotal_progress\x18\x08 \x01(\r\"a\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x15\n\x11STATUS_UNFINISHED\x10\x01\x12\x13\n\x0fSTATUS_FINISHED\x10\x02\x12\x17\n\x13STATUS_REWARD_TAKEN\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_ACHIEVEMENT = DESCRIPTOR.message_types_by_name['Achievement']
_ACHIEVEMENT_STATUS = _ACHIEVEMENT.enum_types_by_name['Status']
Achievement = _reflection.GeneratedProtocolMessageType('Achievement', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENT,
  '__module__' : 'genshin.packet.proto.Achievement_pb2'
  # @@protoc_insertion_point(class_scope:Achievement)
  })
_sym_db.RegisterMessage(Achievement)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ACHIEVEMENT._serialized_start=43
  _ACHIEVEMENT._serialized_end=276
  _ACHIEVEMENT_STATUS._serialized_start=179
  _ACHIEVEMENT_STATUS._serialized_end=276
# @@protoc_insertion_point(module_scope)
