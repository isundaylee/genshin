# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlantFlowerFriendFlowerWishData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ProfilePicture_pb2 as genshin_dot_packet_dot_proto_dot_ProfilePicture__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:genshin/packet/proto/PlantFlowerFriendFlowerWishData.proto\x1a)genshin/packet/proto/ProfilePicture.proto\"\xeb\x01\n\x1fPlantFlowerFriendFlowerWishData\x12(\n\x0fprofile_picture\x18\x03 \x01(\x0b\x32\x0f.ProfilePicture\x12\x0b\n\x03uid\x18\x05 \x01(\r\x12\x10\n\x08nickname\x18\x0e \x01(\t\x12J\n\x0e\x66lower_num_map\x18\x0c \x03(\x0b\x32\x32.PlantFlowerFriendFlowerWishData.FlowerNumMapEntry\x1a\x33\n\x11\x46lowerNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLANTFLOWERFRIENDFLOWERWISHDATA = DESCRIPTOR.message_types_by_name['PlantFlowerFriendFlowerWishData']
_PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY = _PLANTFLOWERFRIENDFLOWERWISHDATA.nested_types_by_name['FlowerNumMapEntry']
PlantFlowerFriendFlowerWishData = _reflection.GeneratedProtocolMessageType('PlantFlowerFriendFlowerWishData', (_message.Message,), {

  'FlowerNumMapEntry' : _reflection.GeneratedProtocolMessageType('FlowerNumMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlantFlowerFriendFlowerWishData_pb2'
    # @@protoc_insertion_point(class_scope:PlantFlowerFriendFlowerWishData.FlowerNumMapEntry)
    })
  ,
  'DESCRIPTOR' : _PLANTFLOWERFRIENDFLOWERWISHDATA,
  '__module__' : 'genshin.packet.proto.PlantFlowerFriendFlowerWishData_pb2'
  # @@protoc_insertion_point(class_scope:PlantFlowerFriendFlowerWishData)
  })
_sym_db.RegisterMessage(PlantFlowerFriendFlowerWishData)
_sym_db.RegisterMessage(PlantFlowerFriendFlowerWishData.FlowerNumMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY._options = None
  _PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY._serialized_options = b'8\001'
  _PLANTFLOWERFRIENDFLOWERWISHDATA._serialized_start=106
  _PLANTFLOWERFRIENDFLOWERWISHDATA._serialized_end=341
  _PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY._serialized_start=290
  _PLANTFLOWERFRIENDFLOWERWISHDATA_FLOWERNUMMAPENTRY._serialized_end=341
# @@protoc_insertion_point(module_scope)
