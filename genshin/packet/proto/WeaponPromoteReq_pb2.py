# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WeaponPromoteReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/WeaponPromoteReq.proto\".\n\x10WeaponPromoteReq\x12\x1a\n\x12target_weapon_guid\x18\x05 \x01(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_WEAPONPROMOTEREQ = DESCRIPTOR.message_types_by_name['WeaponPromoteReq']
WeaponPromoteReq = _reflection.GeneratedProtocolMessageType('WeaponPromoteReq', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONPROMOTEREQ,
  '__module__' : 'genshin.packet.proto.WeaponPromoteReq_pb2'
  # @@protoc_insertion_point(class_scope:WeaponPromoteReq)
  })
_sym_db.RegisterMessage(WeaponPromoteReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WEAPONPROMOTEREQ._serialized_start=47
  _WEAPONPROMOTEREQ._serialized_end=93
# @@protoc_insertion_point(module_scope)