# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlessingGetFriendPicListRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BlessingFriendPicData_pb2 as genshin_dot_packet_dot_proto_dot_BlessingFriendPicData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/BlessingGetFriendPicListRsp.proto\x1a\x30genshin/packet/proto/BlessingFriendPicData.proto\"d\n\x1b\x42lessingGetFriendPicListRsp\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x12\x34\n\x14\x66riend_pic_data_list\x18\x06 \x03(\x0b\x32\x16.BlessingFriendPicDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_BLESSINGGETFRIENDPICLISTRSP = DESCRIPTOR.message_types_by_name['BlessingGetFriendPicListRsp']
BlessingGetFriendPicListRsp = _reflection.GeneratedProtocolMessageType('BlessingGetFriendPicListRsp', (_message.Message,), {
  'DESCRIPTOR' : _BLESSINGGETFRIENDPICLISTRSP,
  '__module__' : 'genshin.packet.proto.BlessingGetFriendPicListRsp_pb2'
  # @@protoc_insertion_point(class_scope:BlessingGetFriendPicListRsp)
  })
_sym_db.RegisterMessage(BlessingGetFriendPicListRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BLESSINGGETFRIENDPICLISTRSP._serialized_start=108
  _BLESSINGGETFRIENDPICLISTRSP._serialized_end=208
# @@protoc_insertion_point(module_scope)
