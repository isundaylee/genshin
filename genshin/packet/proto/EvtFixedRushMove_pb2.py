# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtFixedRushMove.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/EvtFixedRushMove.proto\x1a!genshin/packet/proto/Vector.proto\"\xd3\x01\n\x10\x45vtFixedRushMove\x12\x11\n\tentity_id\x18\x0f \x01(\r\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x1a\n\x12need_set_is_in_air\x18\x07 \x01(\x08\x12\x1e\n\x16\x61nimator_state_id_list\x18\x02 \x03(\r\x12\x1b\n\ntarget_pos\x18\t \x01(\x0b\x32\x07.Vector\x12)\n!check_animator_state_on_exit_only\x18\x06 \x01(\x08\x12\x19\n\x11override_collider\x18\r \x01(\tB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTFIXEDRUSHMOVE = DESCRIPTOR.message_types_by_name['EvtFixedRushMove']
EvtFixedRushMove = _reflection.GeneratedProtocolMessageType('EvtFixedRushMove', (_message.Message,), {
  'DESCRIPTOR' : _EVTFIXEDRUSHMOVE,
  '__module__' : 'genshin.packet.proto.EvtFixedRushMove_pb2'
  # @@protoc_insertion_point(class_scope:EvtFixedRushMove)
  })
_sym_db.RegisterMessage(EvtFixedRushMove)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTFIXEDRUSHMOVE._serialized_start=83
  _EVTFIXEDRUSHMOVE._serialized_end=294
# @@protoc_insertion_point(module_scope)