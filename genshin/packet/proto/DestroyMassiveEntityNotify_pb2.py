# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DestroyMassiveEntityNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ClientMassiveEntity_pb2 as genshin_dot_packet_dot_proto_dot_ClientMassiveEntity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/DestroyMassiveEntityNotify.proto\x1a.genshin/packet/proto/ClientMassiveEntity.proto\"O\n\x1a\x44\x65stroyMassiveEntityNotify\x12\x31\n\x13massive_entity_list\x18\x07 \x03(\x0b\x32\x14.ClientMassiveEntityB\x16\n\x14org.sorapointa.protob\x06proto3')



_DESTROYMASSIVEENTITYNOTIFY = DESCRIPTOR.message_types_by_name['DestroyMassiveEntityNotify']
DestroyMassiveEntityNotify = _reflection.GeneratedProtocolMessageType('DestroyMassiveEntityNotify', (_message.Message,), {
  'DESCRIPTOR' : _DESTROYMASSIVEENTITYNOTIFY,
  '__module__' : 'genshin.packet.proto.DestroyMassiveEntityNotify_pb2'
  # @@protoc_insertion_point(class_scope:DestroyMassiveEntityNotify)
  })
_sym_db.RegisterMessage(DestroyMassiveEntityNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DESTROYMASSIVEENTITYNOTIFY._serialized_start=105
  _DESTROYMASSIVEENTITYNOTIFY._serialized_end=184
# @@protoc_insertion_point(module_scope)
