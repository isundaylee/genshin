# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeMarkPointNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeMarkPointSceneData_pb2 as genshin_dot_packet_dot_proto_dot_HomeMarkPointSceneData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/HomeMarkPointNotify.proto\x1a\x31genshin/packet/proto/HomeMarkPointSceneData.proto\"L\n\x13HomeMarkPointNotify\x12\x35\n\x14mark_point_data_list\x18\x0c \x03(\x0b\x32\x17.HomeMarkPointSceneDataB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_HOMEMARKPOINTNOTIFY = DESCRIPTOR.message_types_by_name['HomeMarkPointNotify']
HomeMarkPointNotify = _reflection.GeneratedProtocolMessageType('HomeMarkPointNotify', (_message.Message,), {
  'DESCRIPTOR' : _HOMEMARKPOINTNOTIFY,
  '__module__' : 'genshin.packet.proto.HomeMarkPointNotify_pb2'
  # @@protoc_insertion_point(class_scope:HomeMarkPointNotify)
  })
_sym_db.RegisterMessage(HomeMarkPointNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _HOMEMARKPOINTNOTIFY._serialized_start=101
  _HOMEMARKPOINTNOTIFY._serialized_end=177
# @@protoc_insertion_point(module_scope)
