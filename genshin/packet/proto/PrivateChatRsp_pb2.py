# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PrivateChatRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/PrivateChatRsp.proto\"A\n\x0ePrivateChatRsp\x12\x1e\n\x16\x63hat_forbidden_endtime\x18\x0c \x01(\r\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PRIVATECHATRSP = DESCRIPTOR.message_types_by_name['PrivateChatRsp']
PrivateChatRsp = _reflection.GeneratedProtocolMessageType('PrivateChatRsp', (_message.Message,), {
  'DESCRIPTOR' : _PRIVATECHATRSP,
  '__module__' : 'genshin.packet.proto.PrivateChatRsp_pb2'
  # @@protoc_insertion_point(class_scope:PrivateChatRsp)
  })
_sym_db.RegisterMessage(PrivateChatRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PRIVATECHATRSP._serialized_start=45
  _PRIVATECHATRSP._serialized_end=110
# @@protoc_insertion_point(module_scope)