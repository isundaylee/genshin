# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/UnlockPersonalLineRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/UnlockPersonalLineRsp.proto\"r\n\x15UnlockPersonalLineRsp\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x12\x18\n\x10personal_line_id\x18\n \x01(\r\x12\x0f\n\x05level\x18\x0b \x01(\rH\x00\x12\x14\n\nchapter_id\x18\x06 \x01(\rH\x00\x42\x07\n\x05paramB\x16\n\x14org.sorapointa.protob\x06proto3')



_UNLOCKPERSONALLINERSP = DESCRIPTOR.message_types_by_name['UnlockPersonalLineRsp']
UnlockPersonalLineRsp = _reflection.GeneratedProtocolMessageType('UnlockPersonalLineRsp', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKPERSONALLINERSP,
  '__module__' : 'genshin.packet.proto.UnlockPersonalLineRsp_pb2'
  # @@protoc_insertion_point(class_scope:UnlockPersonalLineRsp)
  })
_sym_db.RegisterMessage(UnlockPersonalLineRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _UNLOCKPERSONALLINERSP._serialized_start=52
  _UNLOCKPERSONALLINERSP._serialized_end=166
# @@protoc_insertion_point(module_scope)
