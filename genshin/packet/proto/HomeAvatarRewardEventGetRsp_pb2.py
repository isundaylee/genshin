# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeAvatarRewardEventGetRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/HomeAvatarRewardEventGetRsp.proto\x1a$genshin/packet/proto/ItemParam.proto\"_\n\x1bHomeAvatarRewardEventGetRsp\x12\x1d\n\titem_list\x18\x04 \x03(\x0b\x32\n.ItemParam\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEAVATARREWARDEVENTGETRSP = DESCRIPTOR.message_types_by_name['HomeAvatarRewardEventGetRsp']
HomeAvatarRewardEventGetRsp = _reflection.GeneratedProtocolMessageType('HomeAvatarRewardEventGetRsp', (_message.Message,), {
  'DESCRIPTOR' : _HOMEAVATARREWARDEVENTGETRSP,
  '__module__' : 'genshin.packet.proto.HomeAvatarRewardEventGetRsp_pb2'
  # @@protoc_insertion_point(class_scope:HomeAvatarRewardEventGetRsp)
  })
_sym_db.RegisterMessage(HomeAvatarRewardEventGetRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEAVATARREWARDEVENTGETRSP._serialized_start=96
  _HOMEAVATARREWARDEVENTGETRSP._serialized_end=191
# @@protoc_insertion_point(module_scope)
