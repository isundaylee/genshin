# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityActionGenerateElemBall.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/AbilityActionGenerateElemBall.proto\x1a!genshin/packet/proto/Vector.proto\"\\\n\x1d\x41\x62ilityActionGenerateElemBall\x12\x0f\n\x07room_id\x18\x02 \x01(\r\x12\x14\n\x03pos\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x14\n\x03rot\x18\r \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ABILITYACTIONGENERATEELEMBALL = DESCRIPTOR.message_types_by_name['AbilityActionGenerateElemBall']
AbilityActionGenerateElemBall = _reflection.GeneratedProtocolMessageType('AbilityActionGenerateElemBall', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYACTIONGENERATEELEMBALL,
  '__module__' : 'genshin.packet.proto.AbilityActionGenerateElemBall_pb2'
  # @@protoc_insertion_point(class_scope:AbilityActionGenerateElemBall)
  })
_sym_db.RegisterMessage(AbilityActionGenerateElemBall)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ABILITYACTIONGENERATEELEMBALL._serialized_start=95
  _ABILITYACTIONGENERATEELEMBALL._serialized_end=187
# @@protoc_insertion_point(module_scope)
