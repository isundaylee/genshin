# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CoopReward.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/CoopReward.proto\"v\n\nCoopReward\x12\n\n\x02id\x18\x05 \x01(\r\x12 \n\x05state\x18\x06 \x01(\x0e\x32\x11.CoopReward.State\":\n\x05State\x12\x10\n\x0cSTATE_UNLOCK\x10\x00\x12\x0e\n\nSTATE_LOCK\x10\x01\x12\x0f\n\x0bSTATE_TAKEN\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_COOPREWARD = DESCRIPTOR.message_types_by_name['CoopReward']
_COOPREWARD_STATE = _COOPREWARD.enum_types_by_name['State']
CoopReward = _reflection.GeneratedProtocolMessageType('CoopReward', (_message.Message,), {
  'DESCRIPTOR' : _COOPREWARD,
  '__module__' : 'genshin.packet.proto.CoopReward_pb2'
  # @@protoc_insertion_point(class_scope:CoopReward)
  })
_sym_db.RegisterMessage(CoopReward)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _COOPREWARD._serialized_start=41
  _COOPREWARD._serialized_end=159
  _COOPREWARD_STATE._serialized_start=101
  _COOPREWARD_STATE._serialized_end=159
# @@protoc_insertion_point(module_scope)
