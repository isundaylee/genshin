# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetOpActivityInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import OpActivityInfo_pb2 as genshin_dot_packet_dot_proto_dot_OpActivityInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/GetOpActivityInfoRsp.proto\x1a)genshin/packet/proto/OpActivityInfo.proto\"W\n\x14GetOpActivityInfoRsp\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12.\n\x15op_activity_info_list\x18\x07 \x03(\x0b\x32\x0f.OpActivityInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_GETOPACTIVITYINFORSP = DESCRIPTOR.message_types_by_name['GetOpActivityInfoRsp']
GetOpActivityInfoRsp = _reflection.GeneratedProtocolMessageType('GetOpActivityInfoRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETOPACTIVITYINFORSP,
  '__module__' : 'genshin.packet.proto.GetOpActivityInfoRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetOpActivityInfoRsp)
  })
_sym_db.RegisterMessage(GetOpActivityInfoRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETOPACTIVITYINFORSP._serialized_start=94
  _GETOPACTIVITYINFORSP._serialized_end=181
# @@protoc_insertion_point(module_scope)
