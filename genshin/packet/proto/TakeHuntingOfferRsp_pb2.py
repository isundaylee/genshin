# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TakeHuntingOfferRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HuntingPair_pb2 as genshin_dot_packet_dot_proto_dot_HuntingPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/TakeHuntingOfferRsp.proto\x1a&genshin/packet/proto/HuntingPair.proto\"[\n\x13TakeHuntingOfferRsp\x12\"\n\x0chunting_pair\x18\r \x01(\x0b\x32\x0c.HuntingPair\x12\x0f\n\x07\x63ity_id\x18\x0e \x01(\r\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_TAKEHUNTINGOFFERRSP = DESCRIPTOR.message_types_by_name['TakeHuntingOfferRsp']
TakeHuntingOfferRsp = _reflection.GeneratedProtocolMessageType('TakeHuntingOfferRsp', (_message.Message,), {
  'DESCRIPTOR' : _TAKEHUNTINGOFFERRSP,
  '__module__' : 'genshin.packet.proto.TakeHuntingOfferRsp_pb2'
  # @@protoc_insertion_point(class_scope:TakeHuntingOfferRsp)
  })
_sym_db.RegisterMessage(TakeHuntingOfferRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TAKEHUNTINGOFFERRSP._serialized_start=90
  _TAKEHUNTINGOFFERRSP._serialized_end=181
# @@protoc_insertion_point(module_scope)
