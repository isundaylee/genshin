# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarDieAnimationEndReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/AvatarDieAnimationEndReq.proto\x1a!genshin/packet/proto/Vector.proto\"[\n\x18\x41vatarDieAnimationEndReq\x12\x1b\n\nreborn_pos\x18\x03 \x01(\x0b\x32\x07.Vector\x12\x10\n\x08\x64ie_guid\x18\x07 \x01(\x04\x12\x10\n\x08skill_id\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_AVATARDIEANIMATIONENDREQ = DESCRIPTOR.message_types_by_name['AvatarDieAnimationEndReq']
AvatarDieAnimationEndReq = _reflection.GeneratedProtocolMessageType('AvatarDieAnimationEndReq', (_message.Message,), {
  'DESCRIPTOR' : _AVATARDIEANIMATIONENDREQ,
  '__module__' : 'genshin.packet.proto.AvatarDieAnimationEndReq_pb2'
  # @@protoc_insertion_point(class_scope:AvatarDieAnimationEndReq)
  })
_sym_db.RegisterMessage(AvatarDieAnimationEndReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _AVATARDIEANIMATIONENDREQ._serialized_start=90
  _AVATARDIEANIMATIONENDREQ._serialized_end=181
# @@protoc_insertion_point(module_scope)
