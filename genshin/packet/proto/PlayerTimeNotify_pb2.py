# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerTimeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/PlayerTimeNotify.proto\"O\n\x10PlayerTimeNotify\x12\x13\n\x0bserver_time\x18\x05 \x01(\x04\x12\x13\n\x0bplayer_time\x18\x0b \x01(\x04\x12\x11\n\tis_paused\x18\x0e \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERTIMENOTIFY = DESCRIPTOR.message_types_by_name['PlayerTimeNotify']
PlayerTimeNotify = _reflection.GeneratedProtocolMessageType('PlayerTimeNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERTIMENOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerTimeNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerTimeNotify)
  })
_sym_db.RegisterMessage(PlayerTimeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERTIMENOTIFY._serialized_start=47
  _PLAYERTIMENOTIFY._serialized_end=126
# @@protoc_insertion_point(module_scope)
