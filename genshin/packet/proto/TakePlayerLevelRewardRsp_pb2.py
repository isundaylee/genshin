# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TakePlayerLevelRewardRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/TakePlayerLevelRewardRsp.proto\"M\n\x18TakePlayerLevelRewardRsp\x12\x11\n\treward_id\x18\t \x01(\r\x12\x0f\n\x07retcode\x18\r \x01(\x05\x12\r\n\x05level\x18\x06 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TAKEPLAYERLEVELREWARDRSP = DESCRIPTOR.message_types_by_name['TakePlayerLevelRewardRsp']
TakePlayerLevelRewardRsp = _reflection.GeneratedProtocolMessageType('TakePlayerLevelRewardRsp', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPLAYERLEVELREWARDRSP,
  '__module__' : 'genshin.packet.proto.TakePlayerLevelRewardRsp_pb2'
  # @@protoc_insertion_point(class_scope:TakePlayerLevelRewardRsp)
  })
_sym_db.RegisterMessage(TakePlayerLevelRewardRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TAKEPLAYERLEVELREWARDRSP._serialized_start=55
  _TAKEPLAYERLEVELREWARDRSP._serialized_end=132
# @@protoc_insertion_point(module_scope)
