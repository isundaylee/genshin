# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SetEntityClientDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityClientData_pb2 as genshin_dot_packet_dot_proto_dot_EntityClientData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/SetEntityClientDataNotify.proto\x1a+genshin/packet/proto/EntityClientData.proto\"]\n\x19SetEntityClientDataNotify\x12\x11\n\tentity_id\x18\x0e \x01(\r\x12-\n\x12\x65ntity_client_data\x18\t \x01(\x0b\x32\x11.EntityClientDataB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SETENTITYCLIENTDATANOTIFY = DESCRIPTOR.message_types_by_name['SetEntityClientDataNotify']
SetEntityClientDataNotify = _reflection.GeneratedProtocolMessageType('SetEntityClientDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _SETENTITYCLIENTDATANOTIFY,
  '__module__' : 'genshin.packet.proto.SetEntityClientDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:SetEntityClientDataNotify)
  })
_sym_db.RegisterMessage(SetEntityClientDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SETENTITYCLIENTDATANOTIFY._serialized_start=101
  _SETENTITYCLIENTDATANOTIFY._serialized_end=194
# @@protoc_insertion_point(module_scope)