# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TowerTeam.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$genshin/packet/proto/TowerTeam.proto\"<\n\tTowerTeam\x12\x15\n\rtower_team_id\x18\x03 \x01(\r\x12\x18\n\x10\x61vatar_guid_list\x18\x0e \x03(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_TOWERTEAM = DESCRIPTOR.message_types_by_name['TowerTeam']
TowerTeam = _reflection.GeneratedProtocolMessageType('TowerTeam', (_message.Message,), {
  'DESCRIPTOR' : _TOWERTEAM,
  '__module__' : 'genshin.packet.proto.TowerTeam_pb2'
  # @@protoc_insertion_point(class_scope:TowerTeam)
  })
_sym_db.RegisterMessage(TowerTeam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _TOWERTEAM._serialized_start=40
  _TOWERTEAM._serialized_end=100
# @@protoc_insertion_point(module_scope)
