# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FocusAvatarRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/FocusAvatarRsp.proto\"H\n\x0e\x46ocusAvatarRsp\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x12\x10\n\x08is_focus\x18\x0b \x01(\x08\x12\x13\n\x0b\x61vatar_guid\x18\x04 \x01(\x04\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_FOCUSAVATARRSP = DESCRIPTOR.message_types_by_name['FocusAvatarRsp']
FocusAvatarRsp = _reflection.GeneratedProtocolMessageType('FocusAvatarRsp', (_message.Message,), {
  'DESCRIPTOR' : _FOCUSAVATARRSP,
  '__module__' : 'genshin.packet.proto.FocusAvatarRsp_pb2'
  # @@protoc_insertion_point(class_scope:FocusAvatarRsp)
  })
_sym_db.RegisterMessage(FocusAvatarRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FOCUSAVATARRSP._serialized_start=45
  _FOCUSAVATARRSP._serialized_end=117
# @@protoc_insertion_point(module_scope)
