# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EntityMoveFailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MotionInfo_pb2 as genshin_dot_packet_dot_proto_dot_MotionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/EntityMoveFailInfo.proto\x1a%genshin/packet/proto/MotionInfo.proto\"\x84\x01\n\x12\x45ntityMoveFailInfo\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x12\x12\n\nscene_time\x18\t \x01(\r\x12 \n\x0b\x66\x61il_motion\x18\x0e \x01(\x0b\x32\x0b.MotionInfo\x12\x14\n\x0creliable_seq\x18\x04 \x01(\r\x12\x11\n\tentity_id\x18\n \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_ENTITYMOVEFAILINFO = DESCRIPTOR.message_types_by_name['EntityMoveFailInfo']
EntityMoveFailInfo = _reflection.GeneratedProtocolMessageType('EntityMoveFailInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYMOVEFAILINFO,
  '__module__' : 'genshin.packet.proto.EntityMoveFailInfo_pb2'
  # @@protoc_insertion_point(class_scope:EntityMoveFailInfo)
  })
_sym_db.RegisterMessage(EntityMoveFailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ENTITYMOVEFAILINFO._serialized_start=89
  _ENTITYMOVEFAILINFO._serialized_end=221
# @@protoc_insertion_point(module_scope)