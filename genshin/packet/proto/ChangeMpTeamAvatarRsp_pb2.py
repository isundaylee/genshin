# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ChangeMpTeamAvatarRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/ChangeMpTeamAvatarRsp.proto\"[\n\x15\x43hangeMpTeamAvatarRsp\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x12\x18\n\x10\x61vatar_guid_list\x18\x03 \x03(\x04\x12\x17\n\x0f\x63ur_avatar_guid\x18\r \x01(\x04\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_CHANGEMPTEAMAVATARRSP = DESCRIPTOR.message_types_by_name['ChangeMpTeamAvatarRsp']
ChangeMpTeamAvatarRsp = _reflection.GeneratedProtocolMessageType('ChangeMpTeamAvatarRsp', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEMPTEAMAVATARRSP,
  '__module__' : 'genshin.packet.proto.ChangeMpTeamAvatarRsp_pb2'
  # @@protoc_insertion_point(class_scope:ChangeMpTeamAvatarRsp)
  })
_sym_db.RegisterMessage(ChangeMpTeamAvatarRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CHANGEMPTEAMAVATARRSP._serialized_start=52
  _CHANGEMPTEAMAVATARRSP._serialized_end=143
# @@protoc_insertion_point(module_scope)
