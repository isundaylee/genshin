# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SetUpAvatarTeamRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/SetUpAvatarTeamRsp.proto\"n\n\x12SetUpAvatarTeamRsp\x12\x1d\n\x15\x61vatar_team_guid_list\x18\x01 \x03(\x04\x12\x0f\n\x07team_id\x18\x06 \x01(\r\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x12\x17\n\x0f\x63ur_avatar_guid\x18\r \x01(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SETUPAVATARTEAMRSP = DESCRIPTOR.message_types_by_name['SetUpAvatarTeamRsp']
SetUpAvatarTeamRsp = _reflection.GeneratedProtocolMessageType('SetUpAvatarTeamRsp', (_message.Message,), {
  'DESCRIPTOR' : _SETUPAVATARTEAMRSP,
  '__module__' : 'genshin.packet.proto.SetUpAvatarTeamRsp_pb2'
  # @@protoc_insertion_point(class_scope:SetUpAvatarTeamRsp)
  })
_sym_db.RegisterMessage(SetUpAvatarTeamRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SETUPAVATARTEAMRSP._serialized_start=49
  _SETUPAVATARTEAMRSP._serialized_end=159
# @@protoc_insertion_point(module_scope)