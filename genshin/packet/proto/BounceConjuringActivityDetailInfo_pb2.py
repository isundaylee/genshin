# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BounceConjuringActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BounceConjuringChapterInfo_pb2 as genshin_dot_packet_dot_proto_dot_BounceConjuringChapterInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<genshin/packet/proto/BounceConjuringActivityDetailInfo.proto\x1a\x35genshin/packet/proto/BounceConjuringChapterInfo.proto\"\x92\x01\n!BounceConjuringActivityDetailInfo\x12\x36\n\x11\x63hapter_info_list\x18\x08 \x03(\x0b\x32\x1b.BounceConjuringChapterInfo\x12\x19\n\x11is_content_closed\x18\x0c \x01(\x08\x12\x1a\n\x12\x63ontent_close_time\x18\x07 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_BOUNCECONJURINGACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['BounceConjuringActivityDetailInfo']
BounceConjuringActivityDetailInfo = _reflection.GeneratedProtocolMessageType('BounceConjuringActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _BOUNCECONJURINGACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.BounceConjuringActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:BounceConjuringActivityDetailInfo)
  })
_sym_db.RegisterMessage(BounceConjuringActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BOUNCECONJURINGACTIVITYDETAILINFO._serialized_start=120
  _BOUNCECONJURINGACTIVITYDETAILINFO._serialized_end=266
# @@protoc_insertion_point(module_scope)