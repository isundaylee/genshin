# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerCookRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CookRecipeData_pb2 as genshin_dot_packet_dot_proto_dot_CookRecipeData__pb2
from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/PlayerCookRsp.proto\x1a)genshin/packet/proto/CookRecipeData.proto\x1a$genshin/packet/proto/ItemParam.proto\"\xb4\x01\n\rPlayerCookRsp\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x12$\n\x0brecipe_data\x18\x07 \x01(\x0b\x32\x0f.CookRecipeData\x12\x1d\n\titem_list\x18\x0b \x03(\x0b\x32\n.ItemParam\x12\x13\n\x0bqte_quality\x18\x05 \x01(\r\x12\x12\n\ncook_count\x18\x0c \x01(\r\x12$\n\x10\x65xtral_item_list\x18\x0f \x03(\x0b\x32\n.ItemParamB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERCOOKRSP = DESCRIPTOR.message_types_by_name['PlayerCookRsp']
PlayerCookRsp = _reflection.GeneratedProtocolMessageType('PlayerCookRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERCOOKRSP,
  '__module__' : 'genshin.packet.proto.PlayerCookRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerCookRsp)
  })
_sym_db.RegisterMessage(PlayerCookRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERCOOKRSP._serialized_start=126
  _PLAYERCOOKRSP._serialized_end=306
# @@protoc_insertion_point(module_scope)
