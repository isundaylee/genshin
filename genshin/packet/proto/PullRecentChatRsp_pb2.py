# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PullRecentChatRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChatInfo_pb2 as genshin_dot_packet_dot_proto_dot_ChatInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/PullRecentChatRsp.proto\x1a#genshin/packet/proto/ChatInfo.proto\"B\n\x11PullRecentChatRsp\x12\x1c\n\tchat_info\x18\x0f \x03(\x0b\x32\t.ChatInfo\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PULLRECENTCHATRSP = DESCRIPTOR.message_types_by_name['PullRecentChatRsp']
PullRecentChatRsp = _reflection.GeneratedProtocolMessageType('PullRecentChatRsp', (_message.Message,), {
  'DESCRIPTOR' : _PULLRECENTCHATRSP,
  '__module__' : 'genshin.packet.proto.PullRecentChatRsp_pb2'
  # @@protoc_insertion_point(class_scope:PullRecentChatRsp)
  })
_sym_db.RegisterMessage(PullRecentChatRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PULLRECENTCHATRSP._serialized_start=85
  _PULLRECENTCHATRSP._serialized_end=151
# @@protoc_insertion_point(module_scope)
