# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ChangeAvatarRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/ChangeAvatarRsp.proto\"F\n\x0f\x43hangeAvatarRsp\x12\x10\n\x08skill_id\x18\x03 \x01(\r\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12\x10\n\x08\x63ur_guid\x18\x04 \x01(\x04\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_CHANGEAVATARRSP = DESCRIPTOR.message_types_by_name['ChangeAvatarRsp']
ChangeAvatarRsp = _reflection.GeneratedProtocolMessageType('ChangeAvatarRsp', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEAVATARRSP,
  '__module__' : 'genshin.packet.proto.ChangeAvatarRsp_pb2'
  # @@protoc_insertion_point(class_scope:ChangeAvatarRsp)
  })
_sym_db.RegisterMessage(ChangeAvatarRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CHANGEAVATARRSP._serialized_start=46
  _CHANGEAVATARRSP._serialized_end=116
# @@protoc_insertion_point(module_scope)
