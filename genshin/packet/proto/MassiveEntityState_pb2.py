# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MassiveEntityState.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/MassiveEntityState.proto\"P\n\x12MassiveEntityState\x12\x13\n\x0b\x65ntity_type\x18\x01 \x01(\r\x12\x0e\n\x06obj_id\x18\x02 \x01(\x03\x12\x15\n\relement_state\x18\x03 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_MASSIVEENTITYSTATE = DESCRIPTOR.message_types_by_name['MassiveEntityState']
MassiveEntityState = _reflection.GeneratedProtocolMessageType('MassiveEntityState', (_message.Message,), {
  'DESCRIPTOR' : _MASSIVEENTITYSTATE,
  '__module__' : 'genshin.packet.proto.MassiveEntityState_pb2'
  # @@protoc_insertion_point(class_scope:MassiveEntityState)
  })
_sym_db.RegisterMessage(MassiveEntityState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MASSIVEENTITYSTATE._serialized_start=49
  _MASSIVEENTITYSTATE._serialized_end=129
# @@protoc_insertion_point(module_scope)
