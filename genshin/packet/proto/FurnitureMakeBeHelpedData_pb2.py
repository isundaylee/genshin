# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FurnitureMakeBeHelpedData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ProfilePicture_pb2 as genshin_dot_packet_dot_proto_dot_ProfilePicture__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/FurnitureMakeBeHelpedData.proto\x1a)genshin/packet/proto/ProfilePicture.proto\"\x83\x01\n\x19\x46urnitureMakeBeHelpedData\x12\x0c\n\x04time\x18\x0c \x01(\x07\x12\x0c\n\x04icon\x18\x0b \x01(\r\x12\x0b\n\x03uid\x18\x07 \x01(\r\x12\x13\n\x0bplayer_name\x18\n \x01(\t\x12(\n\x0fprofile_picture\x18\x01 \x01(\x0b\x32\x0f.ProfilePictureB\x16\n\x14org.sorapointa.protob\x06proto3')



_FURNITUREMAKEBEHELPEDDATA = DESCRIPTOR.message_types_by_name['FurnitureMakeBeHelpedData']
FurnitureMakeBeHelpedData = _reflection.GeneratedProtocolMessageType('FurnitureMakeBeHelpedData', (_message.Message,), {
  'DESCRIPTOR' : _FURNITUREMAKEBEHELPEDDATA,
  '__module__' : 'genshin.packet.proto.FurnitureMakeBeHelpedData_pb2'
  # @@protoc_insertion_point(class_scope:FurnitureMakeBeHelpedData)
  })
_sym_db.RegisterMessage(FurnitureMakeBeHelpedData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FURNITUREMAKEBEHELPEDDATA._serialized_start=100
  _FURNITUREMAKEBEHELPEDDATA._serialized_end=231
# @@protoc_insertion_point(module_scope)
