# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FishPoolInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/FishPoolInfo.proto\"O\n\x0c\x46ishPoolInfo\x12\x0f\n\x07pool_id\x18\x01 \x01(\r\x12\x16\n\x0e\x66ish_area_list\x18\x02 \x03(\r\x12\x16\n\x0etoday_fish_num\x18\x03 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_FISHPOOLINFO = DESCRIPTOR.message_types_by_name['FishPoolInfo']
FishPoolInfo = _reflection.GeneratedProtocolMessageType('FishPoolInfo', (_message.Message,), {
  'DESCRIPTOR' : _FISHPOOLINFO,
  '__module__' : 'genshin.packet.proto.FishPoolInfo_pb2'
  # @@protoc_insertion_point(class_scope:FishPoolInfo)
  })
_sym_db.RegisterMessage(FishPoolInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _FISHPOOLINFO._serialized_start=43
  _FISHPOOLINFO._serialized_end=122
# @@protoc_insertion_point(module_scope)