# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneEntitiesMovesReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityMoveInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityMoveInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/SceneEntitiesMovesReq.proto\x1a)genshin/packet/proto/EntityMoveInfo.proto\"G\n\x15SceneEntitiesMovesReq\x12.\n\x15\x65ntity_move_info_list\x18\x0e \x03(\x0b\x32\x0f.EntityMoveInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENEENTITIESMOVESREQ = DESCRIPTOR.message_types_by_name['SceneEntitiesMovesReq']
SceneEntitiesMovesReq = _reflection.GeneratedProtocolMessageType('SceneEntitiesMovesReq', (_message.Message,), {
  'DESCRIPTOR' : _SCENEENTITIESMOVESREQ,
  '__module__' : 'genshin.packet.proto.SceneEntitiesMovesReq_pb2'
  # @@protoc_insertion_point(class_scope:SceneEntitiesMovesReq)
  })
_sym_db.RegisterMessage(SceneEntitiesMovesReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENEENTITIESMOVESREQ._serialized_start=95
  _SCENEENTITIESMOVESREQ._serialized_end=166
# @@protoc_insertion_point(module_scope)