# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SumoEnterDungeonNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SumoDungeonTeam_pb2 as genshin_dot_packet_dot_proto_dot_SumoDungeonTeam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/SumoEnterDungeonNotify.proto\x1a*genshin/packet/proto/SumoDungeonTeam.proto\"\xc3\x01\n\x16SumoEnterDungeonNotify\x12\x13\n\x0b\x61\x63tivity_id\x18\x0f \x01(\r\x12+\n\x11\x64ungeon_team_list\x18\x0b \x03(\x0b\x32\x10.SumoDungeonTeam\x12\x1d\n\x15no_switch_punish_time\x18\n \x01(\r\x12\x1e\n\x16next_valid_switch_time\x18\r \x01(\r\x12\x10\n\x08stage_id\x18\x07 \x01(\r\x12\x16\n\x0e\x63ur_team_index\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_SUMOENTERDUNGEONNOTIFY = DESCRIPTOR.message_types_by_name['SumoEnterDungeonNotify']
SumoEnterDungeonNotify = _reflection.GeneratedProtocolMessageType('SumoEnterDungeonNotify', (_message.Message,), {
  'DESCRIPTOR' : _SUMOENTERDUNGEONNOTIFY,
  '__module__' : 'genshin.packet.proto.SumoEnterDungeonNotify_pb2'
  # @@protoc_insertion_point(class_scope:SumoEnterDungeonNotify)
  })
_sym_db.RegisterMessage(SumoEnterDungeonNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SUMOENTERDUNGEONNOTIFY._serialized_start=98
  _SUMOENTERDUNGEONNOTIFY._serialized_end=293
# @@protoc_insertion_point(module_scope)
