# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarFetterDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AvatarFetterInfo_pb2 as genshin_dot_packet_dot_proto_dot_AvatarFetterInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/AvatarFetterDataNotify.proto\x1a+genshin/packet/proto/AvatarFetterInfo.proto\"\xa6\x01\n\x16\x41vatarFetterDataNotify\x12\x43\n\x0f\x66\x65tter_info_map\x18\x0f \x03(\x0b\x32*.AvatarFetterDataNotify.FetterInfoMapEntry\x1aG\n\x12\x46\x65tterInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.AvatarFetterInfo:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_AVATARFETTERDATANOTIFY = DESCRIPTOR.message_types_by_name['AvatarFetterDataNotify']
_AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY = _AVATARFETTERDATANOTIFY.nested_types_by_name['FetterInfoMapEntry']
AvatarFetterDataNotify = _reflection.GeneratedProtocolMessageType('AvatarFetterDataNotify', (_message.Message,), {

  'FetterInfoMapEntry' : _reflection.GeneratedProtocolMessageType('FetterInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarFetterDataNotify_pb2'
    # @@protoc_insertion_point(class_scope:AvatarFetterDataNotify.FetterInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _AVATARFETTERDATANOTIFY,
  '__module__' : 'genshin.packet.proto.AvatarFetterDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:AvatarFetterDataNotify)
  })
_sym_db.RegisterMessage(AvatarFetterDataNotify)
_sym_db.RegisterMessage(AvatarFetterDataNotify.FetterInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY._options = None
  _AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY._serialized_options = b'8\001'
  _AVATARFETTERDATANOTIFY._serialized_start=99
  _AVATARFETTERDATANOTIFY._serialized_end=265
  _AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY._serialized_start=194
  _AVATARFETTERDATANOTIFY_FETTERINFOMAPENTRY._serialized_end=265
# @@protoc_insertion_point(module_scope)
