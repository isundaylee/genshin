# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetBlossomBriefInfoListRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BlossomBriefInfo_pb2 as genshin_dot_packet_dot_proto_dot_BlossomBriefInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/GetBlossomBriefInfoListRsp.proto\x1a+genshin/packet/proto/BlossomBriefInfo.proto\"Y\n\x1aGetBlossomBriefInfoListRsp\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x12*\n\x0f\x62rief_info_list\x18\x0b \x03(\x0b\x32\x11.BlossomBriefInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_GETBLOSSOMBRIEFINFOLISTRSP = DESCRIPTOR.message_types_by_name['GetBlossomBriefInfoListRsp']
GetBlossomBriefInfoListRsp = _reflection.GeneratedProtocolMessageType('GetBlossomBriefInfoListRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOSSOMBRIEFINFOLISTRSP,
  '__module__' : 'genshin.packet.proto.GetBlossomBriefInfoListRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetBlossomBriefInfoListRsp)
  })
_sym_db.RegisterMessage(GetBlossomBriefInfoListRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETBLOSSOMBRIEFINFOLISTRSP._serialized_start=102
  _GETBLOSSOMBRIEFINFOLISTRSP._serialized_end=191
# @@protoc_insertion_point(module_scope)
