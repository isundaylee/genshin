# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/NpcPositionInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/NpcPositionInfo.proto\x1a!genshin/packet/proto/Vector.proto\"7\n\x0fNpcPositionInfo\x12\x0e\n\x06npc_id\x18\x01 \x01(\r\x12\x14\n\x03pos\x18\x02 \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_NPCPOSITIONINFO = DESCRIPTOR.message_types_by_name['NpcPositionInfo']
NpcPositionInfo = _reflection.GeneratedProtocolMessageType('NpcPositionInfo', (_message.Message,), {
  'DESCRIPTOR' : _NPCPOSITIONINFO,
  '__module__' : 'genshin.packet.proto.NpcPositionInfo_pb2'
  # @@protoc_insertion_point(class_scope:NpcPositionInfo)
  })
_sym_db.RegisterMessage(NpcPositionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _NPCPOSITIONINFO._serialized_start=81
  _NPCPOSITIONINFO._serialized_end=136
# @@protoc_insertion_point(module_scope)
