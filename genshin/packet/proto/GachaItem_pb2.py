# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GachaItem.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import GachaTransferItem_pb2 as genshin_dot_packet_dot_proto_dot_GachaTransferItem__pb2
from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$genshin/packet/proto/GachaItem.proto\x1a,genshin/packet/proto/GachaTransferItem.proto\x1a$genshin/packet/proto/ItemParam.proto\"\xaf\x01\n\tGachaItem\x12\x1f\n\x0bgacha_item_\x18\x07 \x01(\x0b\x32\n.ItemParam\x12\x19\n\x11is_gacha_item_new\x18\x06 \x01(\x08\x12\x15\n\ris_flash_card\x18\x08 \x01(\x08\x12#\n\x0ftoken_item_list\x18\t \x03(\x0b\x32\n.ItemParam\x12*\n\x0etransfer_items\x18\x0c \x03(\x0b\x32\x12.GachaTransferItemB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GACHAITEM = DESCRIPTOR.message_types_by_name['GachaItem']
GachaItem = _reflection.GeneratedProtocolMessageType('GachaItem', (_message.Message,), {
  'DESCRIPTOR' : _GACHAITEM,
  '__module__' : 'genshin.packet.proto.GachaItem_pb2'
  # @@protoc_insertion_point(class_scope:GachaItem)
  })
_sym_db.RegisterMessage(GachaItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GACHAITEM._serialized_start=125
  _GACHAITEM._serialized_end=300
# @@protoc_insertion_point(module_scope)
