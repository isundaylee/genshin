# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PersonalSceneJumpRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/PersonalSceneJumpRsp.proto\x1a!genshin/packet/proto/Vector.proto\"Y\n\x14PersonalSceneJumpRsp\x12\x15\n\rdest_scene_id\x18\x05 \x01(\r\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x12\x19\n\x08\x64\x65st_pos\x18\x0b \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_PERSONALSCENEJUMPRSP = DESCRIPTOR.message_types_by_name['PersonalSceneJumpRsp']
PersonalSceneJumpRsp = _reflection.GeneratedProtocolMessageType('PersonalSceneJumpRsp', (_message.Message,), {
  'DESCRIPTOR' : _PERSONALSCENEJUMPRSP,
  '__module__' : 'genshin.packet.proto.PersonalSceneJumpRsp_pb2'
  # @@protoc_insertion_point(class_scope:PersonalSceneJumpRsp)
  })
_sym_db.RegisterMessage(PersonalSceneJumpRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PERSONALSCENEJUMPRSP._serialized_start=86
  _PERSONALSCENEJUMPRSP._serialized_end=175
# @@protoc_insertion_point(module_scope)
