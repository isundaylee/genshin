# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TeamEntityInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/TeamEntityInfo.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\"u\n\x0eTeamEntityInfo\x12\x19\n\x11\x61uthority_peer_id\x18\n \x01(\r\x12\x30\n\x11team_ability_info\x18\t \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x16\n\x0eteam_entity_id\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TEAMENTITYINFO = DESCRIPTOR.message_types_by_name['TeamEntityInfo']
TeamEntityInfo = _reflection.GeneratedProtocolMessageType('TeamEntityInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMENTITYINFO,
  '__module__' : 'genshin.packet.proto.TeamEntityInfo_pb2'
  # @@protoc_insertion_point(class_scope:TeamEntityInfo)
  })
_sym_db.RegisterMessage(TeamEntityInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TEAMENTITYINFO._serialized_start=94
  _TEAMENTITYINFO._serialized_end=211
# @@protoc_insertion_point(module_scope)
