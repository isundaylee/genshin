# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerGameTimeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/PlayerGameTimeNotify.proto\"G\n\x14PlayerGameTimeNotify\x12\x0b\n\x03uid\x18\x07 \x01(\r\x12\x11\n\tgame_time\x18\x03 \x01(\r\x12\x0f\n\x07is_home\x18\r \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERGAMETIMENOTIFY = DESCRIPTOR.message_types_by_name['PlayerGameTimeNotify']
PlayerGameTimeNotify = _reflection.GeneratedProtocolMessageType('PlayerGameTimeNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERGAMETIMENOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerGameTimeNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerGameTimeNotify)
  })
_sym_db.RegisterMessage(PlayerGameTimeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERGAMETIMENOTIFY._serialized_start=51
  _PLAYERGAMETIMENOTIFY._serialized_end=122
# @@protoc_insertion_point(module_scope)