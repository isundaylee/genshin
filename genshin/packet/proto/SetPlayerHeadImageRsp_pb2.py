# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SetPlayerHeadImageRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ProfilePicture_pb2 as genshin_dot_packet_dot_proto_dot_ProfilePicture__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/SetPlayerHeadImageRsp.proto\x1a)genshin/packet/proto/ProfilePicture.proto\"e\n\x15SetPlayerHeadImageRsp\x12(\n\x0fprofile_picture\x18\x06 \x01(\x0b\x32\x0f.ProfilePicture\x12\x11\n\tavatar_id\x18\x05 \x01(\r\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SETPLAYERHEADIMAGERSP = DESCRIPTOR.message_types_by_name['SetPlayerHeadImageRsp']
SetPlayerHeadImageRsp = _reflection.GeneratedProtocolMessageType('SetPlayerHeadImageRsp', (_message.Message,), {
  'DESCRIPTOR' : _SETPLAYERHEADIMAGERSP,
  '__module__' : 'genshin.packet.proto.SetPlayerHeadImageRsp_pb2'
  # @@protoc_insertion_point(class_scope:SetPlayerHeadImageRsp)
  })
_sym_db.RegisterMessage(SetPlayerHeadImageRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SETPLAYERHEADIMAGERSP._serialized_start=95
  _SETPLAYERHEADIMAGERSP._serialized_end=196
# @@protoc_insertion_point(module_scope)
