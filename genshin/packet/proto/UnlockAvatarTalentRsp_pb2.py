# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/UnlockAvatarTalentRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/UnlockAvatarTalentRsp.proto\"P\n\x15UnlockAvatarTalentRsp\x12\x11\n\ttalent_id\x18\x02 \x01(\r\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x12\x13\n\x0b\x61vatar_guid\x18\n \x01(\x04\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_UNLOCKAVATARTALENTRSP = DESCRIPTOR.message_types_by_name['UnlockAvatarTalentRsp']
UnlockAvatarTalentRsp = _reflection.GeneratedProtocolMessageType('UnlockAvatarTalentRsp', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKAVATARTALENTRSP,
  '__module__' : 'genshin.packet.proto.UnlockAvatarTalentRsp_pb2'
  # @@protoc_insertion_point(class_scope:UnlockAvatarTalentRsp)
  })
_sym_db.RegisterMessage(UnlockAvatarTalentRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _UNLOCKAVATARTALENTRSP._serialized_start=52
  _UNLOCKAVATARTALENTRSP._serialized_end=132
# @@protoc_insertion_point(module_scope)
