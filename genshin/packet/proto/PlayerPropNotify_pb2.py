# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerPropNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PropValue_pb2 as genshin_dot_packet_dot_proto_dot_PropValue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/PlayerPropNotify.proto\x1a$genshin/packet/proto/PropValue.proto\"\x80\x01\n\x10PlayerPropNotify\x12\x30\n\x08prop_map\x18\r \x03(\x0b\x32\x1e.PlayerPropNotify.PropMapEntry\x1a:\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERPROPNOTIFY = DESCRIPTOR.message_types_by_name['PlayerPropNotify']
_PLAYERPROPNOTIFY_PROPMAPENTRY = _PLAYERPROPNOTIFY.nested_types_by_name['PropMapEntry']
PlayerPropNotify = _reflection.GeneratedProtocolMessageType('PlayerPropNotify', (_message.Message,), {

  'PropMapEntry' : _reflection.GeneratedProtocolMessageType('PropMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLAYERPROPNOTIFY_PROPMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlayerPropNotify_pb2'
    # @@protoc_insertion_point(class_scope:PlayerPropNotify.PropMapEntry)
    })
  ,
  'DESCRIPTOR' : _PLAYERPROPNOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerPropNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerPropNotify)
  })
_sym_db.RegisterMessage(PlayerPropNotify)
_sym_db.RegisterMessage(PlayerPropNotify.PropMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERPROPNOTIFY_PROPMAPENTRY._options = None
  _PLAYERPROPNOTIFY_PROPMAPENTRY._serialized_options = b'8\001'
  _PLAYERPROPNOTIFY._serialized_start=86
  _PLAYERPROPNOTIFY._serialized_end=214
  _PLAYERPROPNOTIFY_PROPMAPENTRY._serialized_start=156
  _PLAYERPROPNOTIFY_PROPMAPENTRY._serialized_end=214
# @@protoc_insertion_point(module_scope)
