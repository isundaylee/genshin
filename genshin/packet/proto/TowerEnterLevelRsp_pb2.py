# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TowerEnterLevelRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/TowerEnterLevelRsp.proto\"h\n\x12TowerEnterLevelRsp\x12\x1a\n\x12tower_buff_id_list\x18\n \x03(\r\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x13\n\x0blevel_index\x18\x0e \x01(\r\x12\x10\n\x08\x66loor_id\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TOWERENTERLEVELRSP = DESCRIPTOR.message_types_by_name['TowerEnterLevelRsp']
TowerEnterLevelRsp = _reflection.GeneratedProtocolMessageType('TowerEnterLevelRsp', (_message.Message,), {
  'DESCRIPTOR' : _TOWERENTERLEVELRSP,
  '__module__' : 'genshin.packet.proto.TowerEnterLevelRsp_pb2'
  # @@protoc_insertion_point(class_scope:TowerEnterLevelRsp)
  })
_sym_db.RegisterMessage(TowerEnterLevelRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TOWERENTERLEVELRSP._serialized_start=49
  _TOWERENTERLEVELRSP._serialized_end=153
# @@protoc_insertion_point(module_scope)
