# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FurnitureMakeHelpRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FurnitureMakeHelpData_pb2 as genshin_dot_packet_dot_proto_dot_FurnitureMakeHelpData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/FurnitureMakeHelpRsp.proto\x1a\x30genshin/packet/proto/FurnitureMakeHelpData.proto\"W\n\x14\x46urnitureMakeHelpRsp\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12.\n\x0ehelp_data_list\x18\x06 \x03(\x0b\x32\x16.FurnitureMakeHelpDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_FURNITUREMAKEHELPRSP = DESCRIPTOR.message_types_by_name['FurnitureMakeHelpRsp']
FurnitureMakeHelpRsp = _reflection.GeneratedProtocolMessageType('FurnitureMakeHelpRsp', (_message.Message,), {
  'DESCRIPTOR' : _FURNITUREMAKEHELPRSP,
  '__module__' : 'genshin.packet.proto.FurnitureMakeHelpRsp_pb2'
  # @@protoc_insertion_point(class_scope:FurnitureMakeHelpRsp)
  })
_sym_db.RegisterMessage(FurnitureMakeHelpRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FURNITUREMAKEHELPRSP._serialized_start=101
  _FURNITUREMAKEHELPRSP._serialized_end=188
# @@protoc_insertion_point(module_scope)