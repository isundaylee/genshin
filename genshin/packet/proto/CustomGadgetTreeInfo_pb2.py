# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CustomGadgetTreeInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CustomCommonNodeInfo_pb2 as genshin_dot_packet_dot_proto_dot_CustomCommonNodeInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/CustomGadgetTreeInfo.proto\x1a/genshin/packet/proto/CustomCommonNodeInfo.proto\"@\n\x14\x43ustomGadgetTreeInfo\x12(\n\tnode_list\x18\x01 \x03(\x0b\x32\x15.CustomCommonNodeInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_CUSTOMGADGETTREEINFO = DESCRIPTOR.message_types_by_name['CustomGadgetTreeInfo']
CustomGadgetTreeInfo = _reflection.GeneratedProtocolMessageType('CustomGadgetTreeInfo', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMGADGETTREEINFO,
  '__module__' : 'genshin.packet.proto.CustomGadgetTreeInfo_pb2'
  # @@protoc_insertion_point(class_scope:CustomGadgetTreeInfo)
  })
_sym_db.RegisterMessage(CustomGadgetTreeInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CUSTOMGADGETTREEINFO._serialized_start=100
  _CUSTOMGADGETTREEINFO._serialized_end=164
# @@protoc_insertion_point(module_scope)
