# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AbilityInvocationsNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityInvokeEntry_pb2 as genshin_dot_packet_dot_proto_dot_AbilityInvokeEntry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/AbilityInvocationsNotify.proto\x1a-genshin/packet/proto/AbilityInvokeEntry.proto\"@\n\x18\x41\x62ilityInvocationsNotify\x12$\n\x07invokes\x18\x02 \x03(\x0b\x32\x13.AbilityInvokeEntryB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ABILITYINVOCATIONSNOTIFY = DESCRIPTOR.message_types_by_name['AbilityInvocationsNotify']
AbilityInvocationsNotify = _reflection.GeneratedProtocolMessageType('AbilityInvocationsNotify', (_message.Message,), {
  'DESCRIPTOR' : _ABILITYINVOCATIONSNOTIFY,
  '__module__' : 'genshin.packet.proto.AbilityInvocationsNotify_pb2'
  # @@protoc_insertion_point(class_scope:AbilityInvocationsNotify)
  })
_sym_db.RegisterMessage(AbilityInvocationsNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ABILITYINVOCATIONSNOTIFY._serialized_start=102
  _ABILITYINVOCATIONSNOTIFY._serialized_end=166
# @@protoc_insertion_point(module_scope)
