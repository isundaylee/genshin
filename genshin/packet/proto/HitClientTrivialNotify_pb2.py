# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HitClientTrivialNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/HitClientTrivialNotify.proto\x1a!genshin/packet/proto/Vector.proto\"L\n\x16HitClientTrivialNotify\x12\x19\n\x08position\x18\x0b \x01(\x0b\x32\x07.Vector\x12\x17\n\x0fowner_entity_id\x18\x0c \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_HITCLIENTTRIVIALNOTIFY = DESCRIPTOR.message_types_by_name['HitClientTrivialNotify']
HitClientTrivialNotify = _reflection.GeneratedProtocolMessageType('HitClientTrivialNotify', (_message.Message,), {
  'DESCRIPTOR' : _HITCLIENTTRIVIALNOTIFY,
  '__module__' : 'genshin.packet.proto.HitClientTrivialNotify_pb2'
  # @@protoc_insertion_point(class_scope:HitClientTrivialNotify)
  })
_sym_db.RegisterMessage(HitClientTrivialNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HITCLIENTTRIVIALNOTIFY._serialized_start=88
  _HITCLIENTTRIVIALNOTIFY._serialized_end=164
# @@protoc_insertion_point(module_scope)
