# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ArenaChallengeFinishNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ArenaChallengeChildChallengeInfo_pb2 as genshin_dot_packet_dot_proto_dot_ArenaChallengeChildChallengeInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/ArenaChallengeFinishNotify.proto\x1a;genshin/packet/proto/ArenaChallengeChildChallengeInfo.proto\"\xac\x01\n\x1a\x41renaChallengeFinishNotify\x12\x1d\n\x15\x61rena_challenge_level\x18\r \x01(\r\x12\x1a\n\x12\x61rena_challenge_id\x18\x03 \x01(\r\x12?\n\x14\x63hild_challenge_list\x18\x02 \x03(\x0b\x32!.ArenaChallengeChildChallengeInfo\x12\x12\n\nis_success\x18\x0c \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_ARENACHALLENGEFINISHNOTIFY = DESCRIPTOR.message_types_by_name['ArenaChallengeFinishNotify']
ArenaChallengeFinishNotify = _reflection.GeneratedProtocolMessageType('ArenaChallengeFinishNotify', (_message.Message,), {
  'DESCRIPTOR' : _ARENACHALLENGEFINISHNOTIFY,
  '__module__' : 'genshin.packet.proto.ArenaChallengeFinishNotify_pb2'
  # @@protoc_insertion_point(class_scope:ArenaChallengeFinishNotify)
  })
_sym_db.RegisterMessage(ArenaChallengeFinishNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ARENACHALLENGEFINISHNOTIFY._serialized_start=119
  _ARENACHALLENGEFINISHNOTIFY._serialized_end=291
# @@protoc_insertion_point(module_scope)
