# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtMonsterDoBlink.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/EvtMonsterDoBlink.proto\x1a!genshin/packet/proto/Vector.proto\"`\n\x11\x45vtMonsterDoBlink\x12\x1b\n\ntarget_rot\x18\x03 \x01(\x0b\x32\x07.Vector\x12\x1b\n\ntarget_pos\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x11\n\tentity_id\x18\x02 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTMONSTERDOBLINK = DESCRIPTOR.message_types_by_name['EvtMonsterDoBlink']
EvtMonsterDoBlink = _reflection.GeneratedProtocolMessageType('EvtMonsterDoBlink', (_message.Message,), {
  'DESCRIPTOR' : _EVTMONSTERDOBLINK,
  '__module__' : 'genshin.packet.proto.EvtMonsterDoBlink_pb2'
  # @@protoc_insertion_point(class_scope:EvtMonsterDoBlink)
  })
_sym_db.RegisterMessage(EvtMonsterDoBlink)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTMONSTERDOBLINK._serialized_start=83
  _EVTMONSTERDOBLINK._serialized_end=179
# @@protoc_insertion_point(module_scope)
