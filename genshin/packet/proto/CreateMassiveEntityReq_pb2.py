# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CreateMassiveEntityReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ClientMassiveEntity_pb2 as genshin_dot_packet_dot_proto_dot_ClientMassiveEntity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/CreateMassiveEntityReq.proto\x1a.genshin/packet/proto/ClientMassiveEntity.proto\"K\n\x16\x43reateMassiveEntityReq\x12\x31\n\x13massive_entity_list\x18\x01 \x03(\x0b\x32\x14.ClientMassiveEntityB\x16\n\x14org.sorapointa.protob\x06proto3')



_CREATEMASSIVEENTITYREQ = DESCRIPTOR.message_types_by_name['CreateMassiveEntityReq']
CreateMassiveEntityReq = _reflection.GeneratedProtocolMessageType('CreateMassiveEntityReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMASSIVEENTITYREQ,
  '__module__' : 'genshin.packet.proto.CreateMassiveEntityReq_pb2'
  # @@protoc_insertion_point(class_scope:CreateMassiveEntityReq)
  })
_sym_db.RegisterMessage(CreateMassiveEntityReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CREATEMASSIVEENTITYREQ._serialized_start=101
  _CREATEMASSIVEENTITYREQ._serialized_end=176
# @@protoc_insertion_point(module_scope)
