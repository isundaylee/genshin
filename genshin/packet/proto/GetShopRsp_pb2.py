# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetShopRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Shop_pb2 as genshin_dot_packet_dot_proto_dot_Shop__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/GetShopRsp.proto\x1a\x1fgenshin/packet/proto/Shop.proto\"2\n\nGetShopRsp\x12\x13\n\x04shop\x18\x0b \x01(\x0b\x32\x05.Shop\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETSHOPRSP = DESCRIPTOR.message_types_by_name['GetShopRsp']
GetShopRsp = _reflection.GeneratedProtocolMessageType('GetShopRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETSHOPRSP,
  '__module__' : 'genshin.packet.proto.GetShopRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetShopRsp)
  })
_sym_db.RegisterMessage(GetShopRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETSHOPRSP._serialized_start=74
  _GETSHOPRSP._serialized_end=124
# @@protoc_insertion_point(module_scope)