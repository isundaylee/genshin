# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneEntityDisappearNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import VisionType_pb2 as genshin_dot_packet_dot_proto_dot_VisionType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/SceneEntityDisappearNotify.proto\x1a%genshin/packet/proto/VisionType.proto\"e\n\x1aSceneEntityDisappearNotify\x12\r\n\x05param\x18\x06 \x01(\r\x12\x13\n\x0b\x65ntity_list\x18\x01 \x03(\r\x12#\n\x0e\x64isappear_type\x18\x02 \x01(\x0e\x32\x0b.VisionTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENEENTITYDISAPPEARNOTIFY = DESCRIPTOR.message_types_by_name['SceneEntityDisappearNotify']
SceneEntityDisappearNotify = _reflection.GeneratedProtocolMessageType('SceneEntityDisappearNotify', (_message.Message,), {
  'DESCRIPTOR' : _SCENEENTITYDISAPPEARNOTIFY,
  '__module__' : 'genshin.packet.proto.SceneEntityDisappearNotify_pb2'
  # @@protoc_insertion_point(class_scope:SceneEntityDisappearNotify)
  })
_sym_db.RegisterMessage(SceneEntityDisappearNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENEENTITYDISAPPEARNOTIFY._serialized_start=96
  _SCENEENTITYDISAPPEARNOTIFY._serialized_end=197
# @@protoc_insertion_point(module_scope)
