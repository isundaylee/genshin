# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FishAttractNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/FishAttractNotify.proto\x1a!genshin/packet/proto/Vector.proto\"L\n\x11\x46ishAttractNotify\x12\x14\n\x0c\x66ish_id_list\x18\x03 \x03(\r\x12\x14\n\x03pos\x18\t \x01(\x0b\x32\x07.Vector\x12\x0b\n\x03uid\x18\x02 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_FISHATTRACTNOTIFY = DESCRIPTOR.message_types_by_name['FishAttractNotify']
FishAttractNotify = _reflection.GeneratedProtocolMessageType('FishAttractNotify', (_message.Message,), {
  'DESCRIPTOR' : _FISHATTRACTNOTIFY,
  '__module__' : 'genshin.packet.proto.FishAttractNotify_pb2'
  # @@protoc_insertion_point(class_scope:FishAttractNotify)
  })
_sym_db.RegisterMessage(FishAttractNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FISHATTRACTNOTIFY._serialized_start=83
  _FISHATTRACTNOTIFY._serialized_end=159
# @@protoc_insertion_point(module_scope)
