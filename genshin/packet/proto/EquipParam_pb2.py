# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EquipParam.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/EquipParam.proto\"Z\n\nEquipParam\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x10\n\x08item_num\x18\x02 \x01(\r\x12\x12\n\nitem_level\x18\x03 \x01(\r\x12\x15\n\rpromote_level\x18\x04 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EQUIPPARAM = DESCRIPTOR.message_types_by_name['EquipParam']
EquipParam = _reflection.GeneratedProtocolMessageType('EquipParam', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPPARAM,
  '__module__' : 'genshin.packet.proto.EquipParam_pb2'
  # @@protoc_insertion_point(class_scope:EquipParam)
  })
_sym_db.RegisterMessage(EquipParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EQUIPPARAM._serialized_start=41
  _EQUIPPARAM._serialized_end=131
# @@protoc_insertion_point(module_scope)
