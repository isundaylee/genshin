# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TryEnterHomeReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/TryEnterHomeReq.proto\";\n\x0fTryEnterHomeReq\x12\x12\n\ntarget_uid\x18\x03 \x01(\r\x12\x14\n\x0ctarget_point\x18\t \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_TRYENTERHOMEREQ = DESCRIPTOR.message_types_by_name['TryEnterHomeReq']
TryEnterHomeReq = _reflection.GeneratedProtocolMessageType('TryEnterHomeReq', (_message.Message,), {
  'DESCRIPTOR' : _TRYENTERHOMEREQ,
  '__module__' : 'genshin.packet.proto.TryEnterHomeReq_pb2'
  # @@protoc_insertion_point(class_scope:TryEnterHomeReq)
  })
_sym_db.RegisterMessage(TryEnterHomeReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _TRYENTERHOMEREQ._serialized_start=46
  _TRYENTERHOMEREQ._serialized_end=105
# @@protoc_insertion_point(module_scope)
