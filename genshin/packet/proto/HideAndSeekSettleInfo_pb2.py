# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HideAndSeekSettleInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ExhibitionDisplayInfo_pb2 as genshin_dot_packet_dot_proto_dot_ExhibitionDisplayInfo__pb2
from genshin.packet.proto import ProfilePicture_pb2 as genshin_dot_packet_dot_proto_dot_ProfilePicture__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/HideAndSeekSettleInfo.proto\x1a\x30genshin/packet/proto/ExhibitionDisplayInfo.proto\x1a)genshin/packet/proto/ProfilePicture.proto\"\xb2\x01\n\x15HideAndSeekSettleInfo\x12\x0b\n\x03uid\x18\x02 \x01(\r\x12(\n\x0fprofile_picture\x18\x01 \x01(\x0b\x32\x0f.ProfilePicture\x12)\n\tcard_list\x18\x08 \x03(\x0b\x32\x16.ExhibitionDisplayInfo\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x12\n\nhead_image\x18\x04 \x01(\r\x12\x11\n\tonline_id\x18\n \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_HIDEANDSEEKSETTLEINFO = DESCRIPTOR.message_types_by_name['HideAndSeekSettleInfo']
HideAndSeekSettleInfo = _reflection.GeneratedProtocolMessageType('HideAndSeekSettleInfo', (_message.Message,), {
  'DESCRIPTOR' : _HIDEANDSEEKSETTLEINFO,
  '__module__' : 'genshin.packet.proto.HideAndSeekSettleInfo_pb2'
  # @@protoc_insertion_point(class_scope:HideAndSeekSettleInfo)
  })
_sym_db.RegisterMessage(HideAndSeekSettleInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HIDEANDSEEKSETTLEINFO._serialized_start=146
  _HIDEANDSEEKSETTLEINFO._serialized_end=324
# @@protoc_insertion_point(module_scope)
