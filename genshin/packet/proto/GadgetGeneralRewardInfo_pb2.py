# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GadgetGeneralRewardInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/GadgetGeneralRewardInfo.proto\x1a$genshin/packet/proto/ItemParam.proto\"\x8e\x01\n\x17GadgetGeneralRewardInfo\x12\r\n\x05resin\x18\x01 \x01(\r\x12\x11\n\tdead_time\x18\x02 \x01(\r\x12\x17\n\x0fremain_uid_list\x18\x03 \x03(\r\x12\x18\n\x10qualify_uid_list\x18\x04 \x03(\r\x12\x1e\n\nitem_param\x18\x05 \x01(\x0b\x32\n.ItemParamB\x16\n\x14org.sorapointa.protob\x06proto3')



_GADGETGENERALREWARDINFO = DESCRIPTOR.message_types_by_name['GadgetGeneralRewardInfo']
GadgetGeneralRewardInfo = _reflection.GeneratedProtocolMessageType('GadgetGeneralRewardInfo', (_message.Message,), {
  'DESCRIPTOR' : _GADGETGENERALREWARDINFO,
  '__module__' : 'genshin.packet.proto.GadgetGeneralRewardInfo_pb2'
  # @@protoc_insertion_point(class_scope:GadgetGeneralRewardInfo)
  })
_sym_db.RegisterMessage(GadgetGeneralRewardInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GADGETGENERALREWARDINFO._serialized_start=93
  _GADGETGENERALREWARDINFO._serialized_end=235
# @@protoc_insertion_point(module_scope)
