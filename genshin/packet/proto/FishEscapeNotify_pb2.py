# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FishEscapeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FishEscapeReason_pb2 as genshin_dot_packet_dot_proto_dot_FishEscapeReason__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/FishEscapeNotify.proto\x1a+genshin/packet/proto/FishEscapeReason.proto\x1a!genshin/packet/proto/Vector.proto\"n\n\x10\x46ishEscapeNotify\x12!\n\x06reason\x18\x04 \x01(\x0e\x32\x11.FishEscapeReason\x12\x14\n\x03pos\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x0b\n\x03uid\x18\x0e \x01(\r\x12\x14\n\x0c\x66ish_id_list\x18\x06 \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_FISHESCAPENOTIFY = DESCRIPTOR.message_types_by_name['FishEscapeNotify']
FishEscapeNotify = _reflection.GeneratedProtocolMessageType('FishEscapeNotify', (_message.Message,), {
  'DESCRIPTOR' : _FISHESCAPENOTIFY,
  '__module__' : 'genshin.packet.proto.FishEscapeNotify_pb2'
  # @@protoc_insertion_point(class_scope:FishEscapeNotify)
  })
_sym_db.RegisterMessage(FishEscapeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FISHESCAPENOTIFY._serialized_start=127
  _FISHESCAPENOTIFY._serialized_end=237
# @@protoc_insertion_point(module_scope)
