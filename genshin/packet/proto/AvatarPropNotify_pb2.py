# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarPropNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/AvatarPropNotify.proto\"\x89\x01\n\x10\x41vatarPropNotify\x12\x30\n\x08prop_map\x18\x0e \x03(\x0b\x32\x1e.AvatarPropNotify.PropMapEntry\x12\x13\n\x0b\x61vatar_guid\x18\x0f \x01(\x04\x1a.\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AVATARPROPNOTIFY = DESCRIPTOR.message_types_by_name['AvatarPropNotify']
_AVATARPROPNOTIFY_PROPMAPENTRY = _AVATARPROPNOTIFY.nested_types_by_name['PropMapEntry']
AvatarPropNotify = _reflection.GeneratedProtocolMessageType('AvatarPropNotify', (_message.Message,), {

  'PropMapEntry' : _reflection.GeneratedProtocolMessageType('PropMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATARPROPNOTIFY_PROPMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarPropNotify_pb2'
    # @@protoc_insertion_point(class_scope:AvatarPropNotify.PropMapEntry)
    })
  ,
  'DESCRIPTOR' : _AVATARPROPNOTIFY,
  '__module__' : 'genshin.packet.proto.AvatarPropNotify_pb2'
  # @@protoc_insertion_point(class_scope:AvatarPropNotify)
  })
_sym_db.RegisterMessage(AvatarPropNotify)
_sym_db.RegisterMessage(AvatarPropNotify.PropMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AVATARPROPNOTIFY_PROPMAPENTRY._options = None
  _AVATARPROPNOTIFY_PROPMAPENTRY._serialized_options = b'8\001'
  _AVATARPROPNOTIFY._serialized_start=48
  _AVATARPROPNOTIFY._serialized_end=185
  _AVATARPROPNOTIFY_PROPMAPENTRY._serialized_start=139
  _AVATARPROPNOTIFY_PROPMAPENTRY._serialized_end=185
# @@protoc_insertion_point(module_scope)