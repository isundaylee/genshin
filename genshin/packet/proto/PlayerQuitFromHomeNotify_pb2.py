# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerQuitFromHomeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/PlayerQuitFromHomeNotify.proto\"\xb5\x02\n\x18PlayerQuitFromHomeNotify\x12\x34\n\x06reason\x18\x06 \x01(\x0e\x32$.PlayerQuitFromHomeNotify.QuitReason\"\xe2\x01\n\nQuitReason\x12\x17\n\x13QUIT_REASON_INVALID\x10\x00\x12\x1c\n\x18QUIT_REASON_KICK_BY_HOST\x10\x01\x12 \n\x1cQUIT_REASON_BACK_TO_MY_WORLD\x10\x02\x12\x1c\n\x18QUIT_REASON_HOME_BLOCKED\x10\x03\x12!\n\x1dQUIT_REASON_HOME_IN_EDIT_MODE\x10\x04\x12\x17\n\x13QUIT_REASON_BY_MUIP\x10\x05\x12!\n\x1dQUIT_REASON_CUR_MODULE_CLOSED\x10\x06\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERQUITFROMHOMENOTIFY = DESCRIPTOR.message_types_by_name['PlayerQuitFromHomeNotify']
_PLAYERQUITFROMHOMENOTIFY_QUITREASON = _PLAYERQUITFROMHOMENOTIFY.enum_types_by_name['QuitReason']
PlayerQuitFromHomeNotify = _reflection.GeneratedProtocolMessageType('PlayerQuitFromHomeNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERQUITFROMHOMENOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerQuitFromHomeNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerQuitFromHomeNotify)
  })
_sym_db.RegisterMessage(PlayerQuitFromHomeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERQUITFROMHOMENOTIFY._serialized_start=56
  _PLAYERQUITFROMHOMENOTIFY._serialized_end=365
  _PLAYERQUITFROMHOMENOTIFY_QUITREASON._serialized_start=139
  _PLAYERQUITFROMHOMENOTIFY_QUITREASON._serialized_end=365
# @@protoc_insertion_point(module_scope)
