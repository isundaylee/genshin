# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MarkEntityInMinMapNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/MarkEntityInMinMapNotify.proto\x1a!genshin/packet/proto/Vector.proto\"\\\n\x18MarkEntityInMinMapNotify\x12\x19\n\x08position\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x12\n\nmonster_id\x18\x07 \x01(\r\x12\x11\n\tentity_id\x18\x0e \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MARKENTITYINMINMAPNOTIFY = DESCRIPTOR.message_types_by_name['MarkEntityInMinMapNotify']
MarkEntityInMinMapNotify = _reflection.GeneratedProtocolMessageType('MarkEntityInMinMapNotify', (_message.Message,), {
  'DESCRIPTOR' : _MARKENTITYINMINMAPNOTIFY,
  '__module__' : 'genshin.packet.proto.MarkEntityInMinMapNotify_pb2'
  # @@protoc_insertion_point(class_scope:MarkEntityInMinMapNotify)
  })
_sym_db.RegisterMessage(MarkEntityInMinMapNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MARKENTITYINMINMAPNOTIFY._serialized_start=90
  _MARKENTITYINMINMAPNOTIFY._serialized_end=182
# @@protoc_insertion_point(module_scope)
