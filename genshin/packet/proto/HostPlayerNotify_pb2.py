# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HostPlayerNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/HostPlayerNotify.proto\":\n\x10HostPlayerNotify\x12\x14\n\x0chost_peer_id\x18\r \x01(\r\x12\x10\n\x08host_uid\x18\n \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOSTPLAYERNOTIFY = DESCRIPTOR.message_types_by_name['HostPlayerNotify']
HostPlayerNotify = _reflection.GeneratedProtocolMessageType('HostPlayerNotify', (_message.Message,), {
  'DESCRIPTOR' : _HOSTPLAYERNOTIFY,
  '__module__' : 'genshin.packet.proto.HostPlayerNotify_pb2'
  # @@protoc_insertion_point(class_scope:HostPlayerNotify)
  })
_sym_db.RegisterMessage(HostPlayerNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOSTPLAYERNOTIFY._serialized_start=47
  _HOSTPLAYERNOTIFY._serialized_end=105
# @@protoc_insertion_point(module_scope)
