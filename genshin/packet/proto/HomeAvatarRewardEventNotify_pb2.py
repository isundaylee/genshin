# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeAvatarRewardEventNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeAvatarRewardEventInfo_pb2 as genshin_dot_packet_dot_proto_dot_HomeAvatarRewardEventInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/HomeAvatarRewardEventNotify.proto\x1a\x34genshin/packet/proto/HomeAvatarRewardEventInfo.proto\"\x9b\x01\n\x1bHomeAvatarRewardEventNotify\x12\x18\n\x10is_event_trigger\x18\x04 \x01(\x08\x12\x30\n\x0creward_event\x18\x02 \x01(\x0b\x32\x1a.HomeAvatarRewardEventInfo\x12\x30\n\x0cpending_list\x18\x08 \x03(\x0b\x32\x1a.HomeAvatarRewardEventInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEAVATARREWARDEVENTNOTIFY = DESCRIPTOR.message_types_by_name['HomeAvatarRewardEventNotify']
HomeAvatarRewardEventNotify = _reflection.GeneratedProtocolMessageType('HomeAvatarRewardEventNotify', (_message.Message,), {
  'DESCRIPTOR' : _HOMEAVATARREWARDEVENTNOTIFY,
  '__module__' : 'genshin.packet.proto.HomeAvatarRewardEventNotify_pb2'
  # @@protoc_insertion_point(class_scope:HomeAvatarRewardEventNotify)
  })
_sym_db.RegisterMessage(HomeAvatarRewardEventNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEAVATARREWARDEVENTNOTIFY._serialized_start=113
  _HOMEAVATARREWARDEVENTNOTIFY._serialized_end=268
# @@protoc_insertion_point(module_scope)