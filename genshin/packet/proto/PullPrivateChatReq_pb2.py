# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PullPrivateChatReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/PullPrivateChatReq.proto\"Q\n\x12PullPrivateChatReq\x12\x12\n\ntarget_uid\x18\x05 \x01(\r\x12\x10\n\x08pull_num\x18\x07 \x01(\r\x12\x15\n\rfrom_sequence\x18\x0c \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PULLPRIVATECHATREQ = DESCRIPTOR.message_types_by_name['PullPrivateChatReq']
PullPrivateChatReq = _reflection.GeneratedProtocolMessageType('PullPrivateChatReq', (_message.Message,), {
  'DESCRIPTOR' : _PULLPRIVATECHATREQ,
  '__module__' : 'genshin.packet.proto.PullPrivateChatReq_pb2'
  # @@protoc_insertion_point(class_scope:PullPrivateChatReq)
  })
_sym_db.RegisterMessage(PullPrivateChatReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PULLPRIVATECHATREQ._serialized_start=49
  _PULLPRIVATECHATREQ._serialized_end=130
# @@protoc_insertion_point(module_scope)
