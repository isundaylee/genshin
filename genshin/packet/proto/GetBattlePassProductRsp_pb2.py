# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetBattlePassProductRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/GetBattlePassProductRsp.proto\"\x92\x01\n\x17GetBattlePassProductRsp\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x12%\n\x1d\x62\x61ttle_pass_product_play_type\x18\x02 \x01(\r\x12\x17\n\x0f\x63ur_schedule_id\x18\x0b \x01(\r\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x12\n\nprice_tier\x18\x06 \x01(\tB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETBATTLEPASSPRODUCTRSP = DESCRIPTOR.message_types_by_name['GetBattlePassProductRsp']
GetBattlePassProductRsp = _reflection.GeneratedProtocolMessageType('GetBattlePassProductRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETBATTLEPASSPRODUCTRSP,
  '__module__' : 'genshin.packet.proto.GetBattlePassProductRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetBattlePassProductRsp)
  })
_sym_db.RegisterMessage(GetBattlePassProductRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETBATTLEPASSPRODUCTRSP._serialized_start=55
  _GETBATTLEPASSPRODUCTRSP._serialized_end=201
# @@protoc_insertion_point(module_scope)
