# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Reward.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!genshin/packet/proto/Reward.proto\x1a$genshin/packet/proto/ItemParam.proto\":\n\x06Reward\x12\x11\n\treward_id\x18\x01 \x01(\r\x12\x1d\n\titem_list\x18\x02 \x03(\x0b\x32\n.ItemParamB\x16\n\x14org.sorapointa.protob\x06proto3')



_REWARD = DESCRIPTOR.message_types_by_name['Reward']
Reward = _reflection.GeneratedProtocolMessageType('Reward', (_message.Message,), {
  'DESCRIPTOR' : _REWARD,
  '__module__' : 'genshin.packet.proto.Reward_pb2'
  # @@protoc_insertion_point(class_scope:Reward)
  })
_sym_db.RegisterMessage(Reward)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _REWARD._serialized_start=75
  _REWARD._serialized_end=133
# @@protoc_insertion_point(module_scope)