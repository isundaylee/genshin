# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtDestroyGadgetNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/EvtDestroyGadgetNotify.proto\x1a&genshin/packet/proto/ForwardType.proto\"O\n\x16\x45vtDestroyGadgetNotify\x12\"\n\x0c\x66orward_type\x18\x05 \x01(\x0e\x32\x0c.ForwardType\x12\x11\n\tentity_id\x18\x03 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EVTDESTROYGADGETNOTIFY = DESCRIPTOR.message_types_by_name['EvtDestroyGadgetNotify']
EvtDestroyGadgetNotify = _reflection.GeneratedProtocolMessageType('EvtDestroyGadgetNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTDESTROYGADGETNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtDestroyGadgetNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtDestroyGadgetNotify)
  })
_sym_db.RegisterMessage(EvtDestroyGadgetNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EVTDESTROYGADGETNOTIFY._serialized_start=93
  _EVTDESTROYGADGETNOTIFY._serialized_end=172
# @@protoc_insertion_point(module_scope)
