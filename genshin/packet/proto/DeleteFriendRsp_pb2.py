# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DeleteFriendRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/DeleteFriendRsp.proto\"6\n\x0f\x44\x65leteFriendRsp\x12\x12\n\ntarget_uid\x18\x0e \x01(\r\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_DELETEFRIENDRSP = DESCRIPTOR.message_types_by_name['DeleteFriendRsp']
DeleteFriendRsp = _reflection.GeneratedProtocolMessageType('DeleteFriendRsp', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFRIENDRSP,
  '__module__' : 'genshin.packet.proto.DeleteFriendRsp_pb2'
  # @@protoc_insertion_point(class_scope:DeleteFriendRsp)
  })
_sym_db.RegisterMessage(DeleteFriendRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _DELETEFRIENDRSP._serialized_start=46
  _DELETEFRIENDRSP._serialized_end=100
# @@protoc_insertion_point(module_scope)