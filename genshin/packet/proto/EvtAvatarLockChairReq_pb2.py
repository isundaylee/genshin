# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtAvatarLockChairReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/EvtAvatarLockChairReq.proto\x1a!genshin/packet/proto/Vector.proto\"D\n\x15\x45vtAvatarLockChairReq\x12\x10\n\x08\x63hair_id\x18\x05 \x01(\x04\x12\x19\n\x08position\x18\x08 \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EVTAVATARLOCKCHAIRREQ = DESCRIPTOR.message_types_by_name['EvtAvatarLockChairReq']
EvtAvatarLockChairReq = _reflection.GeneratedProtocolMessageType('EvtAvatarLockChairReq', (_message.Message,), {
  'DESCRIPTOR' : _EVTAVATARLOCKCHAIRREQ,
  '__module__' : 'genshin.packet.proto.EvtAvatarLockChairReq_pb2'
  # @@protoc_insertion_point(class_scope:EvtAvatarLockChairReq)
  })
_sym_db.RegisterMessage(EvtAvatarLockChairReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EVTAVATARLOCKCHAIRREQ._serialized_start=87
  _EVTAVATARLOCKCHAIRREQ._serialized_end=155
# @@protoc_insertion_point(module_scope)
