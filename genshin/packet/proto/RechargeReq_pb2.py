# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RechargeReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlayProduct_pb2 as genshin_dot_packet_dot_proto_dot_PlayProduct__pb2
from genshin.packet.proto import ShopCardProduct_pb2 as genshin_dot_packet_dot_proto_dot_ShopCardProduct__pb2
from genshin.packet.proto import ShopConcertProduct_pb2 as genshin_dot_packet_dot_proto_dot_ShopConcertProduct__pb2
from genshin.packet.proto import ShopMcoinProduct_pb2 as genshin_dot_packet_dot_proto_dot_ShopMcoinProduct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/RechargeReq.proto\x1a&genshin/packet/proto/PlayProduct.proto\x1a*genshin/packet/proto/ShopCardProduct.proto\x1a-genshin/packet/proto/ShopConcertProduct.proto\x1a+genshin/packet/proto/ShopMcoinProduct.proto\"\xb1\x01\n\x0bRechargeReq\x12\"\n\x0cplay_product\x18\n \x01(\x0b\x32\x0c.PlayProduct\x12&\n\x0c\x63\x61rd_product\x18\x08 \x01(\x0b\x32\x10.ShopCardProduct\x12(\n\rmcoin_product\x18\x0e \x01(\x0b\x32\x11.ShopMcoinProduct\x12,\n\x0f\x63oncert_product\x18\x07 \x01(\x0b\x32\x13.ShopConcertProductB\x16\n\x14org.sorapointa.protob\x06proto3')



_RECHARGEREQ = DESCRIPTOR.message_types_by_name['RechargeReq']
RechargeReq = _reflection.GeneratedProtocolMessageType('RechargeReq', (_message.Message,), {
  'DESCRIPTOR' : _RECHARGEREQ,
  '__module__' : 'genshin.packet.proto.RechargeReq_pb2'
  # @@protoc_insertion_point(class_scope:RechargeReq)
  })
_sym_db.RegisterMessage(RechargeReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _RECHARGEREQ._serialized_start=219
  _RECHARGEREQ._serialized_end=396
# @@protoc_insertion_point(module_scope)