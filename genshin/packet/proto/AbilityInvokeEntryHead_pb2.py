# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityInvokeEntryHead.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/AbilityInvokeEntryHead.proto\"\xd5\x01\n\x16\x41\x62ilityInvokeEntryHead\x12 \n\x18modifier_config_local_id\x18\x07 \x01(\x05\x12\x1e\n\x16is_serverbuff_modifier\x18\x02 \x01(\x08\x12\x1c\n\x14instanced_ability_id\x18\x01 \x01(\r\x12\x1d\n\x15instanced_modifier_id\x18\x0c \x01(\r\x12\x10\n\x08local_id\x18\n \x01(\x05\x12\x17\n\x0fserver_buff_uid\x18\x0e \x01(\r\x12\x11\n\ttarget_id\x18\x03 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ABILITYINVOKEENTRYHEAD = DESCRIPTOR.message_types_by_name['AbilityInvokeEntryHead']
AbilityInvokeEntryHead = _reflection.GeneratedProtocolMessageType('AbilityInvokeEntryHead', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYINVOKEENTRYHEAD,
  '__module__' : 'genshin.packet.proto.AbilityInvokeEntryHead_pb2'
  # @@protoc_insertion_point(class_scope:AbilityInvokeEntryHead)
  })
_sym_db.RegisterMessage(AbilityInvokeEntryHead)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ABILITYINVOKEENTRYHEAD._serialized_start=54
  _ABILITYINVOKEENTRYHEAD._serialized_end=267
# @@protoc_insertion_point(module_scope)