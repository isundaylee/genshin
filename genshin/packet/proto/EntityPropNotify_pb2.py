# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EntityPropNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PropValue_pb2 as genshin_dot_packet_dot_proto_dot_PropValue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/EntityPropNotify.proto\x1a$genshin/packet/proto/PropValue.proto\"\x93\x01\n\x10\x45ntityPropNotify\x12\x30\n\x08prop_map\x18\x01 \x03(\x0b\x32\x1e.EntityPropNotify.PropMapEntry\x12\x11\n\tentity_id\x18\x0e \x01(\r\x1a:\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ENTITYPROPNOTIFY = DESCRIPTOR.message_types_by_name['EntityPropNotify']
_ENTITYPROPNOTIFY_PROPMAPENTRY = _ENTITYPROPNOTIFY.nested_types_by_name['PropMapEntry']
EntityPropNotify = _reflection.GeneratedProtocolMessageType('EntityPropNotify', (_message.Message,), {

  'PropMapEntry' : _reflection.GeneratedProtocolMessageType('PropMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTITYPROPNOTIFY_PROPMAPENTRY,
    '__module__' : 'genshin.packet.proto.EntityPropNotify_pb2'
    # @@protoc_insertion_point(class_scope:EntityPropNotify.PropMapEntry)
    })
  ,
  'DESCRIPTOR' : _ENTITYPROPNOTIFY,
  '__module__' : 'genshin.packet.proto.EntityPropNotify_pb2'
  # @@protoc_insertion_point(class_scope:EntityPropNotify)
  })
_sym_db.RegisterMessage(EntityPropNotify)
_sym_db.RegisterMessage(EntityPropNotify.PropMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ENTITYPROPNOTIFY_PROPMAPENTRY._options = None
  _ENTITYPROPNOTIFY_PROPMAPENTRY._serialized_options = b'8\001'
  _ENTITYPROPNOTIFY._serialized_start=86
  _ENTITYPROPNOTIFY._serialized_end=233
  _ENTITYPROPNOTIFY_PROPMAPENTRY._serialized_start=175
  _ENTITYPROPNOTIFY_PROPMAPENTRY._serialized_end=233
# @@protoc_insertion_point(module_scope)
