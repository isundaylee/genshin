# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtCombatSteerMotionInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/EvtCombatSteerMotionInfo.proto\x1a!genshin/packet/proto/Vector.proto\"y\n\x18\x45vtCombatSteerMotionInfo\x12\x14\n\x03pos\x18\x0c \x01(\x0b\x32\x07.Vector\x12\x19\n\x08velocity\x18\n \x01(\x0b\x32\x07.Vector\x12\x11\n\tentity_id\x18\x04 \x01(\r\x12\x19\n\x08\x66\x61\x63\x65_dir\x18\x01 \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTCOMBATSTEERMOTIONINFO = DESCRIPTOR.message_types_by_name['EvtCombatSteerMotionInfo']
EvtCombatSteerMotionInfo = _reflection.GeneratedProtocolMessageType('EvtCombatSteerMotionInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVTCOMBATSTEERMOTIONINFO,
  '__module__' : 'genshin.packet.proto.EvtCombatSteerMotionInfo_pb2'
  # @@protoc_insertion_point(class_scope:EvtCombatSteerMotionInfo)
  })
_sym_db.RegisterMessage(EvtCombatSteerMotionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTCOMBATSTEERMOTIONINFO._serialized_start=90
  _EVTCOMBATSTEERMOTIONINFO._serialized_end=211
# @@protoc_insertion_point(module_scope)
