# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetAllActivatedBargainDataRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BargainSnapshot_pb2 as genshin_dot_packet_dot_proto_dot_BargainSnapshot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/GetAllActivatedBargainDataRsp.proto\x1a*genshin/packet/proto/BargainSnapshot.proto\"Y\n\x1dGetAllActivatedBargainDataRsp\x12\'\n\rsnapshot_list\x18\x05 \x03(\x0b\x32\x10.BargainSnapshot\x12\x0f\n\x07retcode\x18\t \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GETALLACTIVATEDBARGAINDATARSP = DESCRIPTOR.message_types_by_name['GetAllActivatedBargainDataRsp']
GetAllActivatedBargainDataRsp = _reflection.GeneratedProtocolMessageType('GetAllActivatedBargainDataRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETALLACTIVATEDBARGAINDATARSP,
  '__module__' : 'genshin.packet.proto.GetAllActivatedBargainDataRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetAllActivatedBargainDataRsp)
  })
_sym_db.RegisterMessage(GetAllActivatedBargainDataRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETALLACTIVATEDBARGAINDATARSP._serialized_start=104
  _GETALLACTIVATEDBARGAINDATARSP._serialized_end=193
# @@protoc_insertion_point(module_scope)
