# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MechanicusInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Uint32Pair_pb2 as genshin_dot_packet_dot_proto_dot_Uint32Pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/MechanicusInfo.proto\x1a%genshin/packet/proto/Uint32Pair.proto\"\xdf\x01\n\x0eMechanicusInfo\x12)\n\x14gear_level_pair_list\x18\x0e \x03(\x0b\x32\x0b.Uint32Pair\x12\x1d\n\x15open_sequence_id_list\x18\x07 \x03(\r\x12\x0c\n\x04\x63oin\x18\x08 \x01(\r\x12\x18\n\x10punish_over_time\x18\x0c \x01(\r\x12\x15\n\rmechanicus_id\x18\n \x01(\r\x12#\n\x1b\x66inish_difficult_level_list\x18\r \x03(\r\x12\x1f\n\x17is_finish_teach_dungeon\x18\x04 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MECHANICUSINFO = DESCRIPTOR.message_types_by_name['MechanicusInfo']
MechanicusInfo = _reflection.GeneratedProtocolMessageType('MechanicusInfo', (_message.Message,), {
  'DESCRIPTOR' : _MECHANICUSINFO,
  '__module__' : 'genshin.packet.proto.MechanicusInfo_pb2'
  # @@protoc_insertion_point(class_scope:MechanicusInfo)
  })
_sym_db.RegisterMessage(MechanicusInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MECHANICUSINFO._serialized_start=85
  _MECHANICUSINFO._serialized_end=308
# @@protoc_insertion_point(module_scope)
