# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerChatRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/PlayerChatRsp.proto\"@\n\rPlayerChatRsp\x12\x1e\n\x16\x63hat_forbidden_endtime\x18\x0f \x01(\r\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERCHATRSP = DESCRIPTOR.message_types_by_name['PlayerChatRsp']
PlayerChatRsp = _reflection.GeneratedProtocolMessageType('PlayerChatRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERCHATRSP,
  '__module__' : 'genshin.packet.proto.PlayerChatRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerChatRsp)
  })
_sym_db.RegisterMessage(PlayerChatRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERCHATRSP._serialized_start=44
  _PLAYERCHATRSP._serialized_end=108
# @@protoc_insertion_point(module_scope)
