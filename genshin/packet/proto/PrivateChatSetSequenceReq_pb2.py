# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PrivateChatSetSequenceReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/PrivateChatSetSequenceReq.proto\"A\n\x19PrivateChatSetSequenceReq\x12\x12\n\ntarget_uid\x18\x0b \x01(\r\x12\x10\n\x08sequence\x18\x0f \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PRIVATECHATSETSEQUENCEREQ = DESCRIPTOR.message_types_by_name['PrivateChatSetSequenceReq']
PrivateChatSetSequenceReq = _reflection.GeneratedProtocolMessageType('PrivateChatSetSequenceReq', (_message.Message,), {
  'DESCRIPTOR' : _PRIVATECHATSETSEQUENCEREQ,
  '__module__' : 'genshin.packet.proto.PrivateChatSetSequenceReq_pb2'
  # @@protoc_insertion_point(class_scope:PrivateChatSetSequenceReq)
  })
_sym_db.RegisterMessage(PrivateChatSetSequenceReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PRIVATECHATSETSEQUENCEREQ._serialized_start=56
  _PRIVATECHATSETSEQUENCEREQ._serialized_end=121
# @@protoc_insertion_point(module_scope)