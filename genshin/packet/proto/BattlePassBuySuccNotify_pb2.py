# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BattlePassBuySuccNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/BattlePassBuySuccNotify.proto\x1a$genshin/packet/proto/ItemParam.proto\"{\n\x17\x42\x61ttlePassBuySuccNotify\x12\x13\n\x0bschedule_id\x18\x04 \x01(\r\x12\x19\n\x11product_play_type\x18\x0b \x01(\r\x12\x11\n\tadd_point\x18\x0c \x01(\r\x12\x1d\n\titem_list\x18\t \x03(\x0b\x32\n.ItemParamB\x16\n\x14org.sorapointa.protob\x06proto3')



_BATTLEPASSBUYSUCCNOTIFY = DESCRIPTOR.message_types_by_name['BattlePassBuySuccNotify']
BattlePassBuySuccNotify = _reflection.GeneratedProtocolMessageType('BattlePassBuySuccNotify', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPASSBUYSUCCNOTIFY,
  '__module__' : 'genshin.packet.proto.BattlePassBuySuccNotify_pb2'
  # @@protoc_insertion_point(class_scope:BattlePassBuySuccNotify)
  })
_sym_db.RegisterMessage(BattlePassBuySuccNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BATTLEPASSBUYSUCCNOTIFY._serialized_start=92
  _BATTLEPASSBUYSUCCNOTIFY._serialized_end=215
# @@protoc_insertion_point(module_scope)
