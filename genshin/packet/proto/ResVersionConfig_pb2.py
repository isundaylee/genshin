# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ResVersionConfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/ResVersionConfig.proto\"\xa3\x01\n\x10ResVersionConfig\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0f\n\x07relogin\x18\x02 \x01(\x08\x12\x0c\n\x04md_5\x18\x03 \x01(\t\x12\x1a\n\x12release_total_size\x18\x04 \x01(\t\x12\x16\n\x0eversion_suffix\x18\x05 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x06 \x01(\t\x12\x1b\n\x13next_script_version\x18\x07 \x01(\tB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_RESVERSIONCONFIG = DESCRIPTOR.message_types_by_name['ResVersionConfig']
ResVersionConfig = _reflection.GeneratedProtocolMessageType('ResVersionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RESVERSIONCONFIG,
  '__module__' : 'genshin.packet.proto.ResVersionConfig_pb2'
  # @@protoc_insertion_point(class_scope:ResVersionConfig)
  })
_sym_db.RegisterMessage(ResVersionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _RESVERSIONCONFIG._serialized_start=48
  _RESVERSIONCONFIG._serialized_end=211
# @@protoc_insertion_point(module_scope)