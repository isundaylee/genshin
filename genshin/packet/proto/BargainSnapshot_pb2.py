# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BargainSnapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/BargainSnapshot.proto\"h\n\x0f\x42\x61rgainSnapshot\x12\x16\n\x0e\x65xpected_price\x18\x03 \x01(\r\x12\x10\n\x08\x63ur_mood\x18\x0e \x01(\x05\x12\x17\n\x0fprice_low_limit\x18\x02 \x01(\r\x12\x12\n\nbargain_id\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_BARGAINSNAPSHOT = DESCRIPTOR.message_types_by_name['BargainSnapshot']
BargainSnapshot = _reflection.GeneratedProtocolMessageType('BargainSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _BARGAINSNAPSHOT,
  '__module__' : 'genshin.packet.proto.BargainSnapshot_pb2'
  # @@protoc_insertion_point(class_scope:BargainSnapshot)
  })
_sym_db.RegisterMessage(BargainSnapshot)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BARGAINSNAPSHOT._serialized_start=46
  _BARGAINSNAPSHOT._serialized_end=150
# @@protoc_insertion_point(module_scope)