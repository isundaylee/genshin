# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlantFlowerGetCanGiveFriendFlowerRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?genshin/packet/proto/PlantFlowerGetCanGiveFriendFlowerRsp.proto\"\xd2\x01\n$PlantFlowerGetCanGiveFriendFlowerRsp\x12O\n\x0e\x66lower_num_map\x18\x06 \x03(\x0b\x32\x37.PlantFlowerGetCanGiveFriendFlowerRsp.FlowerNumMapEntry\x12\x13\n\x0bschedule_id\x18\x04 \x01(\r\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x1a\x33\n\x11\x46lowerNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP = DESCRIPTOR.message_types_by_name['PlantFlowerGetCanGiveFriendFlowerRsp']
_PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY = _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP.nested_types_by_name['FlowerNumMapEntry']
PlantFlowerGetCanGiveFriendFlowerRsp = _reflection.GeneratedProtocolMessageType('PlantFlowerGetCanGiveFriendFlowerRsp', (_message.Message,), {

  'FlowerNumMapEntry' : _reflection.GeneratedProtocolMessageType('FlowerNumMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlantFlowerGetCanGiveFriendFlowerRsp_pb2'
    # @@protoc_insertion_point(class_scope:PlantFlowerGetCanGiveFriendFlowerRsp.FlowerNumMapEntry)
    })
  ,
  'DESCRIPTOR' : _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP,
  '__module__' : 'genshin.packet.proto.PlantFlowerGetCanGiveFriendFlowerRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlantFlowerGetCanGiveFriendFlowerRsp)
  })
_sym_db.RegisterMessage(PlantFlowerGetCanGiveFriendFlowerRsp)
_sym_db.RegisterMessage(PlantFlowerGetCanGiveFriendFlowerRsp.FlowerNumMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY._options = None
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY._serialized_options = b'8\001'
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP._serialized_start=68
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP._serialized_end=278
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY._serialized_start=227
  _PLANTFLOWERGETCANGIVEFRIENDFLOWERRSP_FLOWERNUMMAPENTRY._serialized_end=278
# @@protoc_insertion_point(module_scope)
