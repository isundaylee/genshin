# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DigActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DigMarkPoint_pb2 as genshin_dot_packet_dot_proto_dot_DigMarkPoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/DigActivityDetailInfo.proto\x1a\'genshin/packet/proto/DigMarkPoint.proto\"l\n\x15\x44igActivityDetailInfo\x12\x15\n\rstage_id_list\x18\x0f \x03(\r\x12*\n\x13\x64ig_mark_point_list\x18\x0b \x03(\x0b\x32\r.DigMarkPoint\x12\x10\n\x08stage_id\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_DIGACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['DigActivityDetailInfo']
DigActivityDetailInfo = _reflection.GeneratedProtocolMessageType('DigActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _DIGACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.DigActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:DigActivityDetailInfo)
  })
_sym_db.RegisterMessage(DigActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DIGACTIVITYDETAILINFO._serialized_start=93
  _DIGACTIVITYDETAILINFO._serialized_end=201
# @@protoc_insertion_point(module_scope)