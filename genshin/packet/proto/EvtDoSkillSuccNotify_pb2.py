# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtDoSkillSuccNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/EvtDoSkillSuccNotify.proto\x1a&genshin/packet/proto/ForwardType.proto\x1a!genshin/packet/proto/Vector.proto\"y\n\x14\x45vtDoSkillSuccNotify\x12\x11\n\tcaster_id\x18\r \x01(\r\x12\"\n\x0c\x66orward_type\x18\n \x01(\x0e\x32\x0c.ForwardType\x12\x18\n\x07\x66orward\x18\x0f \x01(\x0b\x32\x07.Vector\x12\x10\n\x08skill_id\x18\x07 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EVTDOSKILLSUCCNOTIFY = DESCRIPTOR.message_types_by_name['EvtDoSkillSuccNotify']
EvtDoSkillSuccNotify = _reflection.GeneratedProtocolMessageType('EvtDoSkillSuccNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTDOSKILLSUCCNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtDoSkillSuccNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtDoSkillSuccNotify)
  })
_sym_db.RegisterMessage(EvtDoSkillSuccNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EVTDOSKILLSUCCNOTIFY._serialized_start=126
  _EVTDOSKILLSUCCNOTIFY._serialized_end=247
# @@protoc_insertion_point(module_scope)