# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetPlayerSocialDetailRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SocialDetail_pb2 as genshin_dot_packet_dot_proto_dot_SocialDetail__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/GetPlayerSocialDetailRsp.proto\x1a\'genshin/packet/proto/SocialDetail.proto\"O\n\x18GetPlayerSocialDetailRsp\x12\"\n\x0b\x64\x65tail_data\x18\x0c \x01(\x0b\x32\r.SocialDetail\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_GETPLAYERSOCIALDETAILRSP = DESCRIPTOR.message_types_by_name['GetPlayerSocialDetailRsp']
GetPlayerSocialDetailRsp = _reflection.GeneratedProtocolMessageType('GetPlayerSocialDetailRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETPLAYERSOCIALDETAILRSP,
  '__module__' : 'genshin.packet.proto.GetPlayerSocialDetailRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetPlayerSocialDetailRsp)
  })
_sym_db.RegisterMessage(GetPlayerSocialDetailRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GETPLAYERSOCIALDETAILRSP._serialized_start=96
  _GETPLAYERSOCIALDETAILRSP._serialized_end=175
# @@protoc_insertion_point(module_scope)
