# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BounceConjuringSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BounceConjuringGallerySettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_BounceConjuringGallerySettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/BounceConjuringSettleNotify.proto\x1a;genshin/packet/proto/BounceConjuringGallerySettleInfo.proto\"\x80\x02\n\x1b\x42ounceConjuringSettleNotify\x12\x15\n\ris_new_record\x18\x0e \x01(\x08\x12H\n\x0fsettle_info_map\x18\x04 \x03(\x0b\x32/.BounceConjuringSettleNotify.SettleInfoMapEntry\x12\x13\n\x0btotal_score\x18\x02 \x01(\r\x12\x12\n\nchapter_id\x18\r \x01(\r\x1aW\n\x12SettleInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.BounceConjuringGallerySettleInfo:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_BOUNCECONJURINGSETTLENOTIFY = DESCRIPTOR.message_types_by_name['BounceConjuringSettleNotify']
_BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY = _BOUNCECONJURINGSETTLENOTIFY.nested_types_by_name['SettleInfoMapEntry']
BounceConjuringSettleNotify = _reflection.GeneratedProtocolMessageType('BounceConjuringSettleNotify', (_message.Message,), {

  'SettleInfoMapEntry' : _reflection.GeneratedProtocolMessageType('SettleInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.BounceConjuringSettleNotify_pb2'
    # @@protoc_insertion_point(class_scope:BounceConjuringSettleNotify.SettleInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _BOUNCECONJURINGSETTLENOTIFY,
  '__module__' : 'genshin.packet.proto.BounceConjuringSettleNotify_pb2'
  # @@protoc_insertion_point(class_scope:BounceConjuringSettleNotify)
  })
_sym_db.RegisterMessage(BounceConjuringSettleNotify)
_sym_db.RegisterMessage(BounceConjuringSettleNotify.SettleInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY._options = None
  _BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY._serialized_options = b'8\001'
  _BOUNCECONJURINGSETTLENOTIFY._serialized_start=120
  _BOUNCECONJURINGSETTLENOTIFY._serialized_end=376
  _BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY._serialized_start=289
  _BOUNCECONJURINGSETTLENOTIFY_SETTLEINFOMAPENTRY._serialized_end=376
# @@protoc_insertion_point(module_scope)
