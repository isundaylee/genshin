# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerQuitDungeonReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/PlayerQuitDungeonReq.proto\"E\n\x14PlayerQuitDungeonReq\x12\x1b\n\x13is_quit_immediately\x18\n \x01(\x08\x12\x10\n\x08point_id\x18\x07 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERQUITDUNGEONREQ = DESCRIPTOR.message_types_by_name['PlayerQuitDungeonReq']
PlayerQuitDungeonReq = _reflection.GeneratedProtocolMessageType('PlayerQuitDungeonReq', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERQUITDUNGEONREQ,
  '__module__' : 'genshin.packet.proto.PlayerQuitDungeonReq_pb2'
  # @@protoc_insertion_point(class_scope:PlayerQuitDungeonReq)
  })
_sym_db.RegisterMessage(PlayerQuitDungeonReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERQUITDUNGEONREQ._serialized_start=51
  _PLAYERQUITDUNGEONREQ._serialized_end=120
# @@protoc_insertion_point(module_scope)
