# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WearEquipReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/WearEquipReq.proto\"7\n\x0cWearEquipReq\x12\x12\n\nequip_guid\x18\x07 \x01(\x04\x12\x13\n\x0b\x61vatar_guid\x18\x05 \x01(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_WEAREQUIPREQ = DESCRIPTOR.message_types_by_name['WearEquipReq']
WearEquipReq = _reflection.GeneratedProtocolMessageType('WearEquipReq', (_message.Message,), {
  'DESCRIPTOR' : _WEAREQUIPREQ,
  '__module__' : 'genshin.packet.proto.WearEquipReq_pb2'
  # @@protoc_insertion_point(class_scope:WearEquipReq)
  })
_sym_db.RegisterMessage(WearEquipReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WEAREQUIPREQ._serialized_start=43
  _WEAREQUIPREQ._serialized_end=98
# @@protoc_insertion_point(module_scope)