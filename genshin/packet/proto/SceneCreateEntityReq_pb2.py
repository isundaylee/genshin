# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneCreateEntityReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CreateEntityInfo_pb2 as genshin_dot_packet_dot_proto_dot_CreateEntityInfo__pb2
from genshin.packet.proto import CreateReason_pb2 as genshin_dot_packet_dot_proto_dot_CreateReason__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/SceneCreateEntityReq.proto\x1a+genshin/packet/proto/CreateEntityInfo.proto\x1a\'genshin/packet/proto/CreateReason.proto\"|\n\x14SceneCreateEntityReq\x12!\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x11.CreateEntityInfo\x12\"\n\x1ais_destroy_when_disconnect\x18\n \x01(\x08\x12\x1d\n\x06reason\x18\x03 \x01(\x0e\x32\r.CreateReasonB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENECREATEENTITYREQ = DESCRIPTOR.message_types_by_name['SceneCreateEntityReq']
SceneCreateEntityReq = _reflection.GeneratedProtocolMessageType('SceneCreateEntityReq', (_message.Message,), {
  'DESCRIPTOR' : _SCENECREATEENTITYREQ,
  '__module__' : 'genshin.packet.proto.SceneCreateEntityReq_pb2'
  # @@protoc_insertion_point(class_scope:SceneCreateEntityReq)
  })
_sym_db.RegisterMessage(SceneCreateEntityReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENECREATEENTITYREQ._serialized_start=137
  _SCENECREATEENTITYREQ._serialized_end=261
# @@protoc_insertion_point(module_scope)