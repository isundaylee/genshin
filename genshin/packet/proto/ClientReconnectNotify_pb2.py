# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientReconnectNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ClientReconnectReason_pb2 as genshin_dot_packet_dot_proto_dot_ClientReconnectReason__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/ClientReconnectNotify.proto\x1a\x30genshin/packet/proto/ClientReconnectReason.proto\"?\n\x15\x43lientReconnectNotify\x12&\n\x06reason\x18\x06 \x01(\x0e\x32\x16.ClientReconnectReasonB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTRECONNECTNOTIFY = DESCRIPTOR.message_types_by_name['ClientReconnectNotify']
ClientReconnectNotify = _reflection.GeneratedProtocolMessageType('ClientReconnectNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTRECONNECTNOTIFY,
  '__module__' : 'genshin.packet.proto.ClientReconnectNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientReconnectNotify)
  })
_sym_db.RegisterMessage(ClientReconnectNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTRECONNECTNOTIFY._serialized_start=102
  _CLIENTRECONNECTNOTIFY._serialized_end=165
# @@protoc_insertion_point(module_scope)