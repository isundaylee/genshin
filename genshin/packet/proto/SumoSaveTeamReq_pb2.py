# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SumoSaveTeamReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SumoTeamData_pb2 as genshin_dot_packet_dot_proto_dot_SumoTeamData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SumoSaveTeamReq.proto\x1a\'genshin/packet/proto/SumoTeamData.proto\"q\n\x0fSumoSaveTeamReq\x12\x13\n\x0b\x61\x63tivity_id\x18\x0b \x01(\r\x12\x10\n\x08stage_id\x18\r \x01(\r\x12\x15\n\rdifficulty_id\x18\x07 \x01(\r\x12 \n\tteam_list\x18\x0c \x03(\x0b\x32\r.SumoTeamDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_SUMOSAVETEAMREQ = DESCRIPTOR.message_types_by_name['SumoSaveTeamReq']
SumoSaveTeamReq = _reflection.GeneratedProtocolMessageType('SumoSaveTeamReq', (_message.Message,), {
  'DESCRIPTOR' : _SUMOSAVETEAMREQ,
  '__module__' : 'genshin.packet.proto.SumoSaveTeamReq_pb2'
  # @@protoc_insertion_point(class_scope:SumoSaveTeamReq)
  })
_sym_db.RegisterMessage(SumoSaveTeamReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SUMOSAVETEAMREQ._serialized_start=87
  _SUMOSAVETEAMREQ._serialized_end=200
# @@protoc_insertion_point(module_scope)
