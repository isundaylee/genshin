# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ShapeSphere.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/ShapeSphere.proto\x1a!genshin/packet/proto/Vector.proto\"6\n\x0bShapeSphere\x12\x17\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x07.Vector\x12\x0e\n\x06radius\x18\x02 \x01(\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SHAPESPHERE = DESCRIPTOR.message_types_by_name['ShapeSphere']
ShapeSphere = _reflection.GeneratedProtocolMessageType('ShapeSphere', (_message.Message,), {
  'DESCRIPTOR' : _SHAPESPHERE,
  '__module__' : 'genshin.packet.proto.ShapeSphere_pb2'
  # @@protoc_insertion_point(class_scope:ShapeSphere)
  })
_sym_db.RegisterMessage(ShapeSphere)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SHAPESPHERE._serialized_start=77
  _SHAPESPHERE._serialized_end=131
# @@protoc_insertion_point(module_scope)
