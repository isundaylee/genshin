# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DropHintNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/DropHintNotify.proto\x1a!genshin/packet/proto/Vector.proto\"A\n\x0e\x44ropHintNotify\x12\x19\n\x08position\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x14\n\x0citem_id_list\x18\x0e \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_DROPHINTNOTIFY = DESCRIPTOR.message_types_by_name['DropHintNotify']
DropHintNotify = _reflection.GeneratedProtocolMessageType('DropHintNotify', (_message.Message,), {
  'DESCRIPTOR' : _DROPHINTNOTIFY,
  '__module__' : 'genshin.packet.proto.DropHintNotify_pb2'
  # @@protoc_insertion_point(class_scope:DropHintNotify)
  })
_sym_db.RegisterMessage(DropHintNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DROPHINTNOTIFY._serialized_start=80
  _DROPHINTNOTIFY._serialized_end=145
# @@protoc_insertion_point(module_scope)
