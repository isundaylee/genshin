# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SetChatEmojiCollectionReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChatEmojiCollectionData_pb2 as genshin_dot_packet_dot_proto_dot_ChatEmojiCollectionData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/SetChatEmojiCollectionReq.proto\x1a\x32genshin/packet/proto/ChatEmojiCollectionData.proto\"Y\n\x19SetChatEmojiCollectionReq\x12<\n\x1a\x63hat_emoji_collection_data\x18\x0c \x01(\x0b\x32\x18.ChatEmojiCollectionDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_SETCHATEMOJICOLLECTIONREQ = DESCRIPTOR.message_types_by_name['SetChatEmojiCollectionReq']
SetChatEmojiCollectionReq = _reflection.GeneratedProtocolMessageType('SetChatEmojiCollectionReq', (_message.Message,), {
  'DESCRIPTOR' : _SETCHATEMOJICOLLECTIONREQ,
  '__module__' : 'genshin.packet.proto.SetChatEmojiCollectionReq_pb2'
  # @@protoc_insertion_point(class_scope:SetChatEmojiCollectionReq)
  })
_sym_db.RegisterMessage(SetChatEmojiCollectionReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SETCHATEMOJICOLLECTIONREQ._serialized_start=108
  _SETCHATEMOJICOLLECTIONREQ._serialized_end=197
# @@protoc_insertion_point(module_scope)
