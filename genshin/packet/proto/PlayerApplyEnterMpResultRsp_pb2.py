# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerApplyEnterMpResultRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/PlayerApplyEnterMpResultRsp.proto\"c\n\x1bPlayerApplyEnterMpResultRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x11\n\tis_agreed\x18\x03 \x01(\x08\x12\x11\n\tapply_uid\x18\n \x01(\r\x12\r\n\x05param\x18\x0c \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERAPPLYENTERMPRESULTRSP = DESCRIPTOR.message_types_by_name['PlayerApplyEnterMpResultRsp']
PlayerApplyEnterMpResultRsp = _reflection.GeneratedProtocolMessageType('PlayerApplyEnterMpResultRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERAPPLYENTERMPRESULTRSP,
  '__module__' : 'genshin.packet.proto.PlayerApplyEnterMpResultRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerApplyEnterMpResultRsp)
  })
_sym_db.RegisterMessage(PlayerApplyEnterMpResultRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERAPPLYENTERMPRESULTRSP._serialized_start=58
  _PLAYERAPPLYENTERMPRESULTRSP._serialized_end=157
# @@protoc_insertion_point(module_scope)