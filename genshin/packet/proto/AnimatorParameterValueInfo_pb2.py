# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AnimatorParameterValueInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/AnimatorParameterValueInfo.proto\"w\n\x1a\x41nimatorParameterValueInfo\x12\x11\n\tpara_type\x18\x01 \x01(\r\x12\x11\n\x07int_val\x18\x02 \x01(\x05H\x00\x12\x13\n\tfloat_val\x18\x03 \x01(\x02H\x00\x12\x12\n\x08\x62ool_val\x18\x04 \x01(\x08H\x00\x42\n\n\x08para_valB\x16\n\x14org.sorapointa.protob\x06proto3')



_ANIMATORPARAMETERVALUEINFO = DESCRIPTOR.message_types_by_name['AnimatorParameterValueInfo']
AnimatorParameterValueInfo = _reflection.GeneratedProtocolMessageType('AnimatorParameterValueInfo', (_message.Message,), {
  'DESCRIPTOR' : _ANIMATORPARAMETERVALUEINFO,
  '__module__' : 'genshin.packet.proto.AnimatorParameterValueInfo_pb2'
  # @@protoc_insertion_point(class_scope:AnimatorParameterValueInfo)
  })
_sym_db.RegisterMessage(AnimatorParameterValueInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ANIMATORPARAMETERVALUEINFO._serialized_start=57
  _ANIMATORPARAMETERVALUEINFO._serialized_end=176
# @@protoc_insertion_point(module_scope)
