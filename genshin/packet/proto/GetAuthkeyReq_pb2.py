# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetAuthkeyReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/GetAuthkeyReq.proto\"K\n\rGetAuthkeyReq\x12\x12\n\nauth_appid\x18\x0e \x01(\t\x12\x11\n\tsign_type\x18\x07 \x01(\r\x12\x13\n\x0b\x61uthkey_ver\x18\r \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETAUTHKEYREQ = DESCRIPTOR.message_types_by_name['GetAuthkeyReq']
GetAuthkeyReq = _reflection.GeneratedProtocolMessageType('GetAuthkeyReq', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTHKEYREQ,
  '__module__' : 'genshin.packet.proto.GetAuthkeyReq_pb2'
  # @@protoc_insertion_point(class_scope:GetAuthkeyReq)
  })
_sym_db.RegisterMessage(GetAuthkeyReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETAUTHKEYREQ._serialized_start=44
  _GETAUTHKEYREQ._serialized_end=119
# @@protoc_insertion_point(module_scope)
