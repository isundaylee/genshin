# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CreateMassiveEntityNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServerMassiveEntity_pb2 as genshin_dot_packet_dot_proto_dot_ServerMassiveEntity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/CreateMassiveEntityNotify.proto\x1a.genshin/packet/proto/ServerMassiveEntity.proto\"N\n\x19\x43reateMassiveEntityNotify\x12\x31\n\x13massive_entity_list\x18\x0f \x03(\x0b\x32\x14.ServerMassiveEntityB\x16\n\x14org.sorapointa.protob\x06proto3')



_CREATEMASSIVEENTITYNOTIFY = DESCRIPTOR.message_types_by_name['CreateMassiveEntityNotify']
CreateMassiveEntityNotify = _reflection.GeneratedProtocolMessageType('CreateMassiveEntityNotify', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMASSIVEENTITYNOTIFY,
  '__module__' : 'genshin.packet.proto.CreateMassiveEntityNotify_pb2'
  # @@protoc_insertion_point(class_scope:CreateMassiveEntityNotify)
  })
_sym_db.RegisterMessage(CreateMassiveEntityNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CREATEMASSIVEENTITYNOTIFY._serialized_start=104
  _CREATEMASSIVEENTITYNOTIFY._serialized_end=182
# @@protoc_insertion_point(module_scope)
