# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TowerCurLevelRecord.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import TowerTeam_pb2 as genshin_dot_packet_dot_proto_dot_TowerTeam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/TowerCurLevelRecord.proto\x1a$genshin/packet/proto/TowerTeam.proto\"\xae\x01\n\x13TowerCurLevelRecord\x12#\n\x0ftower_team_list\x18\x08 \x03(\x0b\x32\n.TowerTeam\x12\x10\n\x08is_empty\x18\x06 \x01(\x08\x12\x14\n\x0c\x62uff_id_list\x18\x04 \x03(\r\x12\x1b\n\x13Unk2700_CBPNPEBMPOH\x18\x02 \x01(\x08\x12\x17\n\x0f\x63ur_level_index\x18\x01 \x01(\r\x12\x14\n\x0c\x63ur_floor_id\x18\x0f \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TOWERCURLEVELRECORD = DESCRIPTOR.message_types_by_name['TowerCurLevelRecord']
TowerCurLevelRecord = _reflection.GeneratedProtocolMessageType('TowerCurLevelRecord', (_message.Message,), {
  'DESCRIPTOR' : _TOWERCURLEVELRECORD,
  '__module__' : 'genshin.packet.proto.TowerCurLevelRecord_pb2'
  # @@protoc_insertion_point(class_scope:TowerCurLevelRecord)
  })
_sym_db.RegisterMessage(TowerCurLevelRecord)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TOWERCURLEVELRECORD._serialized_start=89
  _TOWERCURLEVELRECORD._serialized_end=263
# @@protoc_insertion_point(module_scope)
