# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerCookReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/PlayerCookReq.proto\"b\n\rPlayerCookReq\x12\x11\n\trecipe_id\x18\x08 \x01(\r\x12\x13\n\x0bqte_quality\x18\x0c \x01(\r\x12\x15\n\rassist_avatar\x18\x0e \x01(\r\x12\x12\n\ncook_count\x18\x01 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERCOOKREQ = DESCRIPTOR.message_types_by_name['PlayerCookReq']
PlayerCookReq = _reflection.GeneratedProtocolMessageType('PlayerCookReq', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERCOOKREQ,
  '__module__' : 'genshin.packet.proto.PlayerCookReq_pb2'
  # @@protoc_insertion_point(class_scope:PlayerCookReq)
  })
_sym_db.RegisterMessage(PlayerCookReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERCOOKREQ._serialized_start=44
  _PLAYERCOOKREQ._serialized_end=142
# @@protoc_insertion_point(module_scope)