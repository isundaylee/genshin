# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BattlePassCycle.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/BattlePassCycle.proto\"J\n\x0f\x42\x61ttlePassCycle\x12\x11\n\tcycle_idx\x18\x03 \x01(\r\x12\x12\n\nbegin_time\x18\r \x01(\r\x12\x10\n\x08\x65nd_time\x18\n \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_BATTLEPASSCYCLE = DESCRIPTOR.message_types_by_name['BattlePassCycle']
BattlePassCycle = _reflection.GeneratedProtocolMessageType('BattlePassCycle', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPASSCYCLE,
  '__module__' : 'genshin.packet.proto.BattlePassCycle_pb2'
  # @@protoc_insertion_point(class_scope:BattlePassCycle)
  })
_sym_db.RegisterMessage(BattlePassCycle)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _BATTLEPASSCYCLE._serialized_start=46
  _BATTLEPASSCYCLE._serialized_end=120
# @@protoc_insertion_point(module_scope)
