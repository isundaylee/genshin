# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HuntingRevealFinalNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HuntingPair_pb2 as genshin_dot_packet_dot_proto_dot_HuntingPair__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/HuntingRevealFinalNotify.proto\x1a&genshin/packet/proto/HuntingPair.proto\x1a!genshin/packet/proto/Vector.proto\"z\n\x18HuntingRevealFinalNotify\x12\x19\n\x11\x66inished_group_id\x18\x05 \x01(\r\x12\"\n\x0chunting_pair\x18\x0b \x01(\x0b\x32\x0c.HuntingPair\x12\x1f\n\x0e\x66inal_position\x18\x02 \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_HUNTINGREVEALFINALNOTIFY = DESCRIPTOR.message_types_by_name['HuntingRevealFinalNotify']
HuntingRevealFinalNotify = _reflection.GeneratedProtocolMessageType('HuntingRevealFinalNotify', (_message.Message,), {
  'DESCRIPTOR' : _HUNTINGREVEALFINALNOTIFY,
  '__module__' : 'genshin.packet.proto.HuntingRevealFinalNotify_pb2'
  # @@protoc_insertion_point(class_scope:HuntingRevealFinalNotify)
  })
_sym_db.RegisterMessage(HuntingRevealFinalNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HUNTINGREVEALFINALNOTIFY._serialized_start=130
  _HUNTINGREVEALFINALNOTIFY._serialized_end=252
# @@protoc_insertion_point(module_scope)
