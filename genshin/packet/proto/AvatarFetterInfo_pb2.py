# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarFetterInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FetterData_pb2 as genshin_dot_packet_dot_proto_dot_FetterData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/AvatarFetterInfo.proto\x1a%genshin/packet/proto/FetterData.proto\"\xad\x01\n\x10\x41vatarFetterInfo\x12\x12\n\nexp_number\x18\x01 \x01(\r\x12\x11\n\texp_level\x18\x02 \x01(\r\x12\x14\n\x0copen_id_list\x18\x03 \x03(\r\x12\x16\n\x0e\x66inish_id_list\x18\x04 \x03(\r\x12\"\n\x1arewarded_fetter_level_list\x18\x05 \x03(\r\x12 \n\x0b\x66\x65tter_list\x18\x06 \x03(\x0b\x32\x0b.FetterDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_AVATARFETTERINFO = DESCRIPTOR.message_types_by_name['AvatarFetterInfo']
AvatarFetterInfo = _reflection.GeneratedProtocolMessageType('AvatarFetterInfo', (_message.Message,), {
  'DESCRIPTOR' : _AVATARFETTERINFO,
  '__module__' : 'genshin.packet.proto.AvatarFetterInfo_pb2'
  # @@protoc_insertion_point(class_scope:AvatarFetterInfo)
  })
_sym_db.RegisterMessage(AvatarFetterInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _AVATARFETTERINFO._serialized_start=87
  _AVATARFETTERINFO._serialized_end=260
# @@protoc_insertion_point(module_scope)
