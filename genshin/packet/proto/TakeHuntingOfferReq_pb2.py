# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TakeHuntingOfferReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HuntingPair_pb2 as genshin_dot_packet_dot_proto_dot_HuntingPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/TakeHuntingOfferReq.proto\x1a&genshin/packet/proto/HuntingPair.proto\"J\n\x13TakeHuntingOfferReq\x12\"\n\x0chunting_pair\x18\x0e \x01(\x0b\x32\x0c.HuntingPair\x12\x0f\n\x07\x63ity_id\x18\x04 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TAKEHUNTINGOFFERREQ = DESCRIPTOR.message_types_by_name['TakeHuntingOfferReq']
TakeHuntingOfferReq = _reflection.GeneratedProtocolMessageType('TakeHuntingOfferReq', (_message.Message,), {
  'DESCRIPTOR' : _TAKEHUNTINGOFFERREQ,
  '__module__' : 'genshin.packet.proto.TakeHuntingOfferReq_pb2'
  # @@protoc_insertion_point(class_scope:TakeHuntingOfferReq)
  })
_sym_db.RegisterMessage(TakeHuntingOfferReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TAKEHUNTINGOFFERREQ._serialized_start=90
  _TAKEHUNTINGOFFERREQ._serialized_end=164
# @@protoc_insertion_point(module_scope)
