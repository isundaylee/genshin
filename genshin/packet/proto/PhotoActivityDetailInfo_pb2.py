# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PhotoActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PhotoStage_pb2 as genshin_dot_packet_dot_proto_dot_PhotoStage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/PhotoActivityDetailInfo.proto\x1a%genshin/packet/proto/PhotoStage.proto\"[\n\x17PhotoActivityDetailInfo\x12\x19\n\x11is_content_closed\x18\x04 \x01(\x08\x12%\n\x10photo_stage_list\x18\x0c \x03(\x0b\x32\x0b.PhotoStageB\x16\n\x14org.sorapointa.protob\x06proto3')



_PHOTOACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['PhotoActivityDetailInfo']
PhotoActivityDetailInfo = _reflection.GeneratedProtocolMessageType('PhotoActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _PHOTOACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.PhotoActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:PhotoActivityDetailInfo)
  })
_sym_db.RegisterMessage(PhotoActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PHOTOACTIVITYDETAILINFO._serialized_start=93
  _PHOTOACTIVITYDETAILINFO._serialized_end=184
# @@protoc_insertion_point(module_scope)
