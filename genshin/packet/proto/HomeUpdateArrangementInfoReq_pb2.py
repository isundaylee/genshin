# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeUpdateArrangementInfoReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeSceneArrangementInfo_pb2 as genshin_dot_packet_dot_proto_dot_HomeSceneArrangementInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/HomeUpdateArrangementInfoReq.proto\x1a\x33genshin/packet/proto/HomeSceneArrangementInfo.proto\"Y\n\x1cHomeUpdateArrangementInfoReq\x12\x39\n\x16scene_arrangement_info\x18\x06 \x01(\x0b\x32\x19.HomeSceneArrangementInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEUPDATEARRANGEMENTINFOREQ = DESCRIPTOR.message_types_by_name['HomeUpdateArrangementInfoReq']
HomeUpdateArrangementInfoReq = _reflection.GeneratedProtocolMessageType('HomeUpdateArrangementInfoReq', (_message.Message,), {
  'DESCRIPTOR' : _HOMEUPDATEARRANGEMENTINFOREQ,
  '__module__' : 'genshin.packet.proto.HomeUpdateArrangementInfoReq_pb2'
  # @@protoc_insertion_point(class_scope:HomeUpdateArrangementInfoReq)
  })
_sym_db.RegisterMessage(HomeUpdateArrangementInfoReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEUPDATEARRANGEMENTINFOREQ._serialized_start=112
  _HOMEUPDATEARRANGEMENTINFOREQ._serialized_end=201
# @@protoc_insertion_point(module_scope)
