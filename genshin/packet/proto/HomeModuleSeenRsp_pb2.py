# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeModuleSeenRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/HomeModuleSeenRsp.proto\"A\n\x11HomeModuleSeenRsp\x12\x1b\n\x13seen_module_id_list\x18\r \x03(\r\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEMODULESEENRSP = DESCRIPTOR.message_types_by_name['HomeModuleSeenRsp']
HomeModuleSeenRsp = _reflection.GeneratedProtocolMessageType('HomeModuleSeenRsp', (_message.Message,), {
  'DESCRIPTOR' : _HOMEMODULESEENRSP,
  '__module__' : 'genshin.packet.proto.HomeModuleSeenRsp_pb2'
  # @@protoc_insertion_point(class_scope:HomeModuleSeenRsp)
  })
_sym_db.RegisterMessage(HomeModuleSeenRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEMODULESEENRSP._serialized_start=48
  _HOMEMODULESEENRSP._serialized_end=113
# @@protoc_insertion_point(module_scope)