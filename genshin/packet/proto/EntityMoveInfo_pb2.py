# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EntityMoveInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MotionInfo_pb2 as genshin_dot_packet_dot_proto_dot_MotionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/EntityMoveInfo.proto\x1a%genshin/packet/proto/MotionInfo.proto\"\x84\x01\n\x0e\x45ntityMoveInfo\x12\x11\n\tentity_id\x18\x01 \x01(\r\x12 \n\x0bmotion_info\x18\x02 \x01(\x0b\x32\x0b.MotionInfo\x12\x12\n\nscene_time\x18\x03 \x01(\r\x12\x14\n\x0creliable_seq\x18\x04 \x01(\r\x12\x13\n\x0bis_reliable\x18\x05 \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ENTITYMOVEINFO = DESCRIPTOR.message_types_by_name['EntityMoveInfo']
EntityMoveInfo = _reflection.GeneratedProtocolMessageType('EntityMoveInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYMOVEINFO,
  '__module__' : 'genshin.packet.proto.EntityMoveInfo_pb2'
  # @@protoc_insertion_point(class_scope:EntityMoveInfo)
  })
_sym_db.RegisterMessage(EntityMoveInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ENTITYMOVEINFO._serialized_start=85
  _ENTITYMOVEINFO._serialized_end=217
# @@protoc_insertion_point(module_scope)
