# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientAbilityInitFinishNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityInvokeEntry_pb2 as genshin_dot_packet_dot_proto_dot_AbilityInvokeEntry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/ClientAbilityInitFinishNotify.proto\x1a-genshin/packet/proto/AbilityInvokeEntry.proto\"X\n\x1d\x43lientAbilityInitFinishNotify\x12$\n\x07invokes\x18\x0e \x03(\x0b\x32\x13.AbilityInvokeEntry\x12\x11\n\tentity_id\x18\x0b \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_CLIENTABILITYINITFINISHNOTIFY = DESCRIPTOR.message_types_by_name['ClientAbilityInitFinishNotify']
ClientAbilityInitFinishNotify = _reflection.GeneratedProtocolMessageType('ClientAbilityInitFinishNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTABILITYINITFINISHNOTIFY,
  '__module__' : 'genshin.packet.proto.ClientAbilityInitFinishNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientAbilityInitFinishNotify)
  })
_sym_db.RegisterMessage(ClientAbilityInitFinishNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _CLIENTABILITYINITFINISHNOTIFY._serialized_start=107
  _CLIENTABILITYINITFINISHNOTIFY._serialized_end=195
# @@protoc_insertion_point(module_scope)
