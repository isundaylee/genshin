# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AskAddFriendNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FriendBrief_pb2 as genshin_dot_packet_dot_proto_dot_FriendBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/AskAddFriendNotify.proto\x1a&genshin/packet/proto/FriendBrief.proto\"S\n\x12\x41skAddFriendNotify\x12)\n\x13target_friend_brief\x18\x0f \x01(\x0b\x32\x0c.FriendBrief\x12\x12\n\ntarget_uid\x18\t \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_ASKADDFRIENDNOTIFY = DESCRIPTOR.message_types_by_name['AskAddFriendNotify']
AskAddFriendNotify = _reflection.GeneratedProtocolMessageType('AskAddFriendNotify', (_message.Message,), {
  'DESCRIPTOR' : _ASKADDFRIENDNOTIFY,
  '__module__' : 'genshin.packet.proto.AskAddFriendNotify_pb2'
  # @@protoc_insertion_point(class_scope:AskAddFriendNotify)
  })
_sym_db.RegisterMessage(AskAddFriendNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ASKADDFRIENDNOTIFY._serialized_start=89
  _ASKADDFRIENDNOTIFY._serialized_end=172
# @@protoc_insertion_point(module_scope)
