# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetNextResourceInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ResVersionConfig_pb2 as genshin_dot_packet_dot_proto_dot_ResVersionConfig__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/GetNextResourceInfoRsp.proto\x1a+genshin/packet/proto/ResVersionConfig.proto\"x\n\x16GetNextResourceInfoRsp\x12\x19\n\x11next_resource_url\x18\x0e \x01(\t\x12\x32\n\x17next_res_version_config\x18\x02 \x01(\x0b\x32\x11.ResVersionConfig\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GETNEXTRESOURCEINFORSP = DESCRIPTOR.message_types_by_name['GetNextResourceInfoRsp']
GetNextResourceInfoRsp = _reflection.GeneratedProtocolMessageType('GetNextResourceInfoRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETNEXTRESOURCEINFORSP,
  '__module__' : 'genshin.packet.proto.GetNextResourceInfoRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetNextResourceInfoRsp)
  })
_sym_db.RegisterMessage(GetNextResourceInfoRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETNEXTRESOURCEINFORSP._serialized_start=98
  _GETNEXTRESOURCEINFORSP._serialized_end=218
# @@protoc_insertion_point(module_scope)
