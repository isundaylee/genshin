# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlantFlowerSetFlowerWishReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/PlantFlowerSetFlowerWishReq.proto\"\xaf\x01\n\x1bPlantFlowerSetFlowerWishReq\x12\x46\n\x0e\x66lower_num_map\x18\x0c \x03(\x0b\x32..PlantFlowerSetFlowerWishReq.FlowerNumMapEntry\x12\x13\n\x0bschedule_id\x18\x05 \x01(\r\x1a\x33\n\x11\x46lowerNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLANTFLOWERSETFLOWERWISHREQ = DESCRIPTOR.message_types_by_name['PlantFlowerSetFlowerWishReq']
_PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY = _PLANTFLOWERSETFLOWERWISHREQ.nested_types_by_name['FlowerNumMapEntry']
PlantFlowerSetFlowerWishReq = _reflection.GeneratedProtocolMessageType('PlantFlowerSetFlowerWishReq', (_message.Message,), {

  'FlowerNumMapEntry' : _reflection.GeneratedProtocolMessageType('FlowerNumMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlantFlowerSetFlowerWishReq_pb2'
    # @@protoc_insertion_point(class_scope:PlantFlowerSetFlowerWishReq.FlowerNumMapEntry)
    })
  ,
  'DESCRIPTOR' : _PLANTFLOWERSETFLOWERWISHREQ,
  '__module__' : 'genshin.packet.proto.PlantFlowerSetFlowerWishReq_pb2'
  # @@protoc_insertion_point(class_scope:PlantFlowerSetFlowerWishReq)
  })
_sym_db.RegisterMessage(PlantFlowerSetFlowerWishReq)
_sym_db.RegisterMessage(PlantFlowerSetFlowerWishReq.FlowerNumMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY._options = None
  _PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY._serialized_options = b'8\001'
  _PLANTFLOWERSETFLOWERWISHREQ._serialized_start=59
  _PLANTFLOWERSETFLOWERWISHREQ._serialized_end=234
  _PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY._serialized_start=183
  _PLANTFLOWERSETFLOWERWISHREQ_FLOWERNUMMAPENTRY._serialized_end=234
# @@protoc_insertion_point(module_scope)
