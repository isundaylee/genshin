# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtAnimatorStateChangedNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EvtAnimatorStateChangedInfo_pb2 as genshin_dot_packet_dot_proto_dot_EvtAnimatorStateChangedInfo__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/EvtAnimatorStateChangedNotify.proto\x1a\x36genshin/packet/proto/EvtAnimatorStateChangedInfo.proto\x1a&genshin/packet/proto/ForwardType.proto\"\x8a\x01\n\x1d\x45vtAnimatorStateChangedNotify\x12\"\n\x0c\x66orward_type\x18\x03 \x01(\x0e\x32\x0c.ForwardType\x12\x45\n\x1f\x65vt_animator_state_changed_info\x18\n \x01(\x0b\x32\x1c.EvtAnimatorStateChangedInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTANIMATORSTATECHANGEDNOTIFY = DESCRIPTOR.message_types_by_name['EvtAnimatorStateChangedNotify']
EvtAnimatorStateChangedNotify = _reflection.GeneratedProtocolMessageType('EvtAnimatorStateChangedNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTANIMATORSTATECHANGEDNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtAnimatorStateChangedNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtAnimatorStateChangedNotify)
  })
_sym_db.RegisterMessage(EvtAnimatorStateChangedNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTANIMATORSTATECHANGEDNOTIFY._serialized_start=157
  _EVTANIMATORSTATECHANGEDNOTIFY._serialized_end=295
# @@protoc_insertion_point(module_scope)
