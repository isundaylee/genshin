# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerOfferingRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2
from genshin.packet.proto import PlayerOfferingData_pb2 as genshin_dot_packet_dot_proto_dot_PlayerOfferingData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/PlayerOfferingRsp.proto\x1a$genshin/packet/proto/ItemParam.proto\x1a-genshin/packet/proto/PlayerOfferingData.proto\"o\n\x11PlayerOfferingRsp\x12\x1d\n\titem_list\x18\x07 \x03(\x0b\x32\n.ItemParam\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x12*\n\roffering_data\x18\n \x01(\x0b\x32\x13.PlayerOfferingDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYEROFFERINGRSP = DESCRIPTOR.message_types_by_name['PlayerOfferingRsp']
PlayerOfferingRsp = _reflection.GeneratedProtocolMessageType('PlayerOfferingRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLAYEROFFERINGRSP,
  '__module__' : 'genshin.packet.proto.PlayerOfferingRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerOfferingRsp)
  })
_sym_db.RegisterMessage(PlayerOfferingRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYEROFFERINGRSP._serialized_start=133
  _PLAYEROFFERINGRSP._serialized_end=244
# @@protoc_insertion_point(module_scope)
