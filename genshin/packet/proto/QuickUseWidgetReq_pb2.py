# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuickUseWidgetReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WidgetCameraInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCameraInfo__pb2
from genshin.packet.proto import WidgetCreateLocationInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCreateLocationInfo__pb2
from genshin.packet.proto import WidgetCreatorInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCreatorInfo__pb2
from genshin.packet.proto import WidgetThunderBirdFeatherInfo_pb2 as genshin_dot_packet_dot_proto_dot_WidgetThunderBirdFeatherInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/QuickUseWidgetReq.proto\x1a+genshin/packet/proto/WidgetCameraInfo.proto\x1a\x33genshin/packet/proto/WidgetCreateLocationInfo.proto\x1a,genshin/packet/proto/WidgetCreatorInfo.proto\x1a\x37genshin/packet/proto/WidgetThunderBirdFeatherInfo.proto\"\xee\x01\n\x11QuickUseWidgetReq\x12\x33\n\rlocation_info\x18\xa4\x05 \x01(\x0b\x32\x19.WidgetCreateLocationInfoH\x00\x12)\n\x0b\x63\x61mera_info\x18\xde\x03 \x01(\x0b\x32\x11.WidgetCameraInfoH\x00\x12+\n\x0c\x63reator_info\x18\xac\x06 \x01(\x0b\x32\x12.WidgetCreatorInfoH\x00\x12\x43\n\x19thunder_bird_feather_info\x18\xc3\x0e \x01(\x0b\x32\x1d.WidgetThunderBirdFeatherInfoH\x00\x42\x07\n\x05paramB\x16\n\x14org.sorapointa.protob\x06proto3')



_QUICKUSEWIDGETREQ = DESCRIPTOR.message_types_by_name['QuickUseWidgetReq']
QuickUseWidgetReq = _reflection.GeneratedProtocolMessageType('QuickUseWidgetReq', (_message.Message,), {
  'DESCRIPTOR' : _QUICKUSEWIDGETREQ,
  '__module__' : 'genshin.packet.proto.QuickUseWidgetReq_pb2'
  # @@protoc_insertion_point(class_scope:QuickUseWidgetReq)
  })
_sym_db.RegisterMessage(QuickUseWidgetReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _QUICKUSEWIDGETREQ._serialized_start=250
  _QUICKUSEWIDGETREQ._serialized_end=488
# @@protoc_insertion_point(module_scope)
