# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtHittingOtherInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AttackResult_pb2 as genshin_dot_packet_dot_proto_dot_AttackResult__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/EvtHittingOtherInfo.proto\x1a\'genshin/packet/proto/AttackResult.proto\"L\n\x13\x45vtHittingOtherInfo\x12$\n\rattack_result\x18\x02 \x01(\x0b\x32\r.AttackResult\x12\x0f\n\x07peer_id\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTHITTINGOTHERINFO = DESCRIPTOR.message_types_by_name['EvtHittingOtherInfo']
EvtHittingOtherInfo = _reflection.GeneratedProtocolMessageType('EvtHittingOtherInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVTHITTINGOTHERINFO,
  '__module__' : 'genshin.packet.proto.EvtHittingOtherInfo_pb2'
  # @@protoc_insertion_point(class_scope:EvtHittingOtherInfo)
  })
_sym_db.RegisterMessage(EvtHittingOtherInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTHITTINGOTHERINFO._serialized_start=91
  _EVTHITTINGOTHERINFO._serialized_end=167
# @@protoc_insertion_point(module_scope)
