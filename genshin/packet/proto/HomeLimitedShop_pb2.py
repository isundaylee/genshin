# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeLimitedShop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeLimitedShopGoods_pb2 as genshin_dot_packet_dot_proto_dot_HomeLimitedShopGoods__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/HomeLimitedShop.proto\x1a/genshin/packet/proto/HomeLimitedShopGoods.proto\"<\n\x0fHomeLimitedShop\x12)\n\ngoods_list\x18\x08 \x03(\x0b\x32\x15.HomeLimitedShopGoodsB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMELIMITEDSHOP = DESCRIPTOR.message_types_by_name['HomeLimitedShop']
HomeLimitedShop = _reflection.GeneratedProtocolMessageType('HomeLimitedShop', (_message.Message,), {
  'DESCRIPTOR' : _HOMELIMITEDSHOP,
  '__module__' : 'genshin.packet.proto.HomeLimitedShop_pb2'
  # @@protoc_insertion_point(class_scope:HomeLimitedShop)
  })
_sym_db.RegisterMessage(HomeLimitedShop)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMELIMITEDSHOP._serialized_start=95
  _HOMELIMITEDSHOP._serialized_end=155
# @@protoc_insertion_point(module_scope)
