# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ForgeStartReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/ForgeStartReq.proto\"I\n\rForgeStartReq\x12\x11\n\tavatar_id\x18\x07 \x01(\r\x12\x10\n\x08\x66orge_id\x18\x04 \x01(\r\x12\x13\n\x0b\x66orge_count\x18\x06 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_FORGESTARTREQ = DESCRIPTOR.message_types_by_name['ForgeStartReq']
ForgeStartReq = _reflection.GeneratedProtocolMessageType('ForgeStartReq', (_message.Message,), {
  'DESCRIPTOR' : _FORGESTARTREQ,
  '__module__' : 'genshin.packet.proto.ForgeStartReq_pb2'
  # @@protoc_insertion_point(class_scope:ForgeStartReq)
  })
_sym_db.RegisterMessage(ForgeStartReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _FORGESTARTREQ._serialized_start=44
  _FORGESTARTREQ._serialized_end=117
# @@protoc_insertion_point(module_scope)