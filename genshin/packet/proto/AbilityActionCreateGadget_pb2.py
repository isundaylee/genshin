# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityActionCreateGadget.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/AbilityActionCreateGadget.proto\x1a!genshin/packet/proto/Vector.proto\"X\n\x19\x41\x62ilityActionCreateGadget\x12\x0f\n\x07room_id\x18\x03 \x01(\r\x12\x14\n\x03rot\x18\x08 \x01(\x0b\x32\x07.Vector\x12\x14\n\x03pos\x18\x0b \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_ABILITYACTIONCREATEGADGET = DESCRIPTOR.message_types_by_name['AbilityActionCreateGadget']
AbilityActionCreateGadget = _reflection.GeneratedProtocolMessageType('AbilityActionCreateGadget', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYACTIONCREATEGADGET,
  '__module__' : 'genshin.packet.proto.AbilityActionCreateGadget_pb2'
  # @@protoc_insertion_point(class_scope:AbilityActionCreateGadget)
  })
_sym_db.RegisterMessage(AbilityActionCreateGadget)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ABILITYACTIONCREATEGADGET._serialized_start=91
  _ABILITYACTIONCREATEGADGET._serialized_end=179
# @@protoc_insertion_point(module_scope)
