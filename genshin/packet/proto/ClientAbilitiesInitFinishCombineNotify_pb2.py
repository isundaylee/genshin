# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientAbilitiesInitFinishCombineNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityAbilityInvokeEntry_pb2 as genshin_dot_packet_dot_proto_dot_EntityAbilityInvokeEntry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgenshin/packet/proto/ClientAbilitiesInitFinishCombineNotify.proto\x1a\x33genshin/packet/proto/EntityAbilityInvokeEntry.proto\"_\n&ClientAbilitiesInitFinishCombineNotify\x12\x35\n\x12\x65ntity_invoke_list\x18\x01 \x03(\x0b\x32\x19.EntityAbilityInvokeEntryB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTABILITIESINITFINISHCOMBINENOTIFY = DESCRIPTOR.message_types_by_name['ClientAbilitiesInitFinishCombineNotify']
ClientAbilitiesInitFinishCombineNotify = _reflection.GeneratedProtocolMessageType('ClientAbilitiesInitFinishCombineNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTABILITIESINITFINISHCOMBINENOTIFY,
  '__module__' : 'genshin.packet.proto.ClientAbilitiesInitFinishCombineNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientAbilitiesInitFinishCombineNotify)
  })
_sym_db.RegisterMessage(ClientAbilitiesInitFinishCombineNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTABILITIESINITFINISHCOMBINENOTIFY._serialized_start=122
  _CLIENTABILITIESINITFINISHCOMBINENOTIFY._serialized_end=217
# @@protoc_insertion_point(module_scope)
