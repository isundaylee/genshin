# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarFightPropNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/AvatarFightPropNotify.proto\"\xa3\x01\n\x15\x41vatarFightPropNotify\x12@\n\x0e\x66ight_prop_map\x18\x08 \x03(\x0b\x32(.AvatarFightPropNotify.FightPropMapEntry\x12\x13\n\x0b\x61vatar_guid\x18\x04 \x01(\x04\x1a\x33\n\x11\x46ightPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AVATARFIGHTPROPNOTIFY = DESCRIPTOR.message_types_by_name['AvatarFightPropNotify']
_AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY = _AVATARFIGHTPROPNOTIFY.nested_types_by_name['FightPropMapEntry']
AvatarFightPropNotify = _reflection.GeneratedProtocolMessageType('AvatarFightPropNotify', (_message.Message,), {

  'FightPropMapEntry' : _reflection.GeneratedProtocolMessageType('FightPropMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarFightPropNotify_pb2'
    # @@protoc_insertion_point(class_scope:AvatarFightPropNotify.FightPropMapEntry)
    })
  ,
  'DESCRIPTOR' : _AVATARFIGHTPROPNOTIFY,
  '__module__' : 'genshin.packet.proto.AvatarFightPropNotify_pb2'
  # @@protoc_insertion_point(class_scope:AvatarFightPropNotify)
  })
_sym_db.RegisterMessage(AvatarFightPropNotify)
_sym_db.RegisterMessage(AvatarFightPropNotify.FightPropMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY._options = None
  _AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY._serialized_options = b'8\001'
  _AVATARFIGHTPROPNOTIFY._serialized_start=53
  _AVATARFIGHTPROPNOTIFY._serialized_end=216
  _AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY._serialized_start=165
  _AVATARFIGHTPROPNOTIFY_FIGHTPROPMAPENTRY._serialized_end=216
# @@protoc_insertion_point(module_scope)