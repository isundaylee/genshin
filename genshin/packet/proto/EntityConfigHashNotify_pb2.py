# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EntityConfigHashNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityConfigHashEntry_pb2 as genshin_dot_packet_dot_proto_dot_EntityConfigHashEntry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/EntityConfigHashNotify.proto\x1a\x30genshin/packet/proto/EntityConfigHashEntry.proto\"\xb2\x01\n\x16\x45ntityConfigHashNotify\x12\x32\n\x12\x61\x62ility_entry_list\x18\x03 \x03(\x0b\x32\x16.EntityConfigHashEntry\x12\x31\n\x11\x61vatar_entry_list\x18\x0f \x03(\x0b\x32\x16.EntityConfigHashEntry\x12\x31\n\x11\x63ombat_entry_list\x18\x08 \x03(\x0b\x32\x16.EntityConfigHashEntryB\x16\n\x14org.sorapointa.protob\x06proto3')



_ENTITYCONFIGHASHNOTIFY = DESCRIPTOR.message_types_by_name['EntityConfigHashNotify']
EntityConfigHashNotify = _reflection.GeneratedProtocolMessageType('EntityConfigHashNotify', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYCONFIGHASHNOTIFY,
  '__module__' : 'genshin.packet.proto.EntityConfigHashNotify_pb2'
  # @@protoc_insertion_point(class_scope:EntityConfigHashNotify)
  })
_sym_db.RegisterMessage(EntityConfigHashNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ENTITYCONFIGHASHNOTIFY._serialized_start=104
  _ENTITYCONFIGHASHNOTIFY._serialized_end=282
# @@protoc_insertion_point(module_scope)
