# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RogueCellInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RogueCellState_pb2 as genshin_dot_packet_dot_proto_dot_RogueCellState__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/RogueCellInfo.proto\x1a)genshin/packet/proto/RogueCellState.proto\"\x7f\n\rRogueCellInfo\x12\x16\n\x0e\x63\x65ll_config_id\x18\x0e \x01(\r\x12\x12\n\ndungeon_id\x18\x04 \x01(\r\x12\x0f\n\x07\x63\x65ll_id\x18\t \x01(\r\x12\x11\n\tcell_type\x18\r \x01(\r\x12\x1e\n\x05state\x18\n \x01(\x0e\x32\x0f.RogueCellStateB\x16\n\x14org.sorapointa.protob\x06proto3')



_ROGUECELLINFO = DESCRIPTOR.message_types_by_name['RogueCellInfo']
RogueCellInfo = _reflection.GeneratedProtocolMessageType('RogueCellInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROGUECELLINFO,
  '__module__' : 'genshin.packet.proto.RogueCellInfo_pb2'
  # @@protoc_insertion_point(class_scope:RogueCellInfo)
  })
_sym_db.RegisterMessage(RogueCellInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ROGUECELLINFO._serialized_start=87
  _ROGUECELLINFO._serialized_end=214
# @@protoc_insertion_point(module_scope)
