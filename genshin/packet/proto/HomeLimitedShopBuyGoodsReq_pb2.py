# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeLimitedShopBuyGoodsReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeLimitedShopGoods_pb2 as genshin_dot_packet_dot_proto_dot_HomeLimitedShopGoods__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/HomeLimitedShopBuyGoodsReq.proto\x1a/genshin/packet/proto/HomeLimitedShopGoods.proto\"U\n\x1aHomeLimitedShopBuyGoodsReq\x12$\n\x05goods\x18\x03 \x01(\x0b\x32\x15.HomeLimitedShopGoods\x12\x11\n\tbuy_count\x18\n \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMELIMITEDSHOPBUYGOODSREQ = DESCRIPTOR.message_types_by_name['HomeLimitedShopBuyGoodsReq']
HomeLimitedShopBuyGoodsReq = _reflection.GeneratedProtocolMessageType('HomeLimitedShopBuyGoodsReq', (_message.Message,), {
  'DESCRIPTOR' : _HOMELIMITEDSHOPBUYGOODSREQ,
  '__module__' : 'genshin.packet.proto.HomeLimitedShopBuyGoodsReq_pb2'
  # @@protoc_insertion_point(class_scope:HomeLimitedShopBuyGoodsReq)
  })
_sym_db.RegisterMessage(HomeLimitedShopBuyGoodsReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMELIMITEDSHOPBUYGOODSREQ._serialized_start=106
  _HOMELIMITEDSHOPBUYGOODSREQ._serialized_end=191
# @@protoc_insertion_point(module_scope)