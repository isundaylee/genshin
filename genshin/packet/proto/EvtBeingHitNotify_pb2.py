# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtBeingHitNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EvtBeingHitInfo_pb2 as genshin_dot_packet_dot_proto_dot_EvtBeingHitInfo__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/EvtBeingHitNotify.proto\x1a*genshin/packet/proto/EvtBeingHitInfo.proto\x1a&genshin/packet/proto/ForwardType.proto\"a\n\x11\x45vtBeingHitNotify\x12\"\n\x0c\x66orward_type\x18\x06 \x01(\x0e\x32\x0c.ForwardType\x12(\n\x0e\x62\x65ing_hit_info\x18\x03 \x01(\x0b\x32\x10.EvtBeingHitInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EVTBEINGHITNOTIFY = DESCRIPTOR.message_types_by_name['EvtBeingHitNotify']
EvtBeingHitNotify = _reflection.GeneratedProtocolMessageType('EvtBeingHitNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTBEINGHITNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtBeingHitNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtBeingHitNotify)
  })
_sym_db.RegisterMessage(EvtBeingHitNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EVTBEINGHITNOTIFY._serialized_start=132
  _EVTBEINGHITNOTIFY._serialized_end=229
# @@protoc_insertion_point(module_scope)
