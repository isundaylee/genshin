# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtCombatForceSetPosInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/EvtCombatForceSetPosInfo.proto\x1a!genshin/packet/proto/Vector.proto\"v\n\x18\x45vtCombatForceSetPosInfo\x12\x0e\n\x06ice_id\x18\t \x01(\r\x12\x1a\n\x12\x63ollider_entity_id\x18\n \x01(\r\x12\x11\n\tentity_id\x18\x06 \x01(\r\x12\x1b\n\ntarget_pos\x18\x01 \x01(\x0b\x32\x07.VectorB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTCOMBATFORCESETPOSINFO = DESCRIPTOR.message_types_by_name['EvtCombatForceSetPosInfo']
EvtCombatForceSetPosInfo = _reflection.GeneratedProtocolMessageType('EvtCombatForceSetPosInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVTCOMBATFORCESETPOSINFO,
  '__module__' : 'genshin.packet.proto.EvtCombatForceSetPosInfo_pb2'
  # @@protoc_insertion_point(class_scope:EvtCombatForceSetPosInfo)
  })
_sym_db.RegisterMessage(EvtCombatForceSetPosInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTCOMBATFORCESETPOSINFO._serialized_start=90
  _EVTCOMBATFORCESETPOSINFO._serialized_end=208
# @@protoc_insertion_point(module_scope)