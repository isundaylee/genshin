# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ChallengeRecordNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChallengeRecord_pb2 as genshin_dot_packet_dot_proto_dot_ChallengeRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/ChallengeRecordNotify.proto\x1a*genshin/packet/proto/ChallengeRecord.proto\"Z\n\x15\x43hallengeRecordNotify\x12\x10\n\x08group_id\x18\x02 \x01(\r\x12/\n\x15\x63hallenge_record_list\x18\x05 \x03(\x0b\x32\x10.ChallengeRecordB\x16\n\x14org.sorapointa.protob\x06proto3')



_CHALLENGERECORDNOTIFY = DESCRIPTOR.message_types_by_name['ChallengeRecordNotify']
ChallengeRecordNotify = _reflection.GeneratedProtocolMessageType('ChallengeRecordNotify', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGERECORDNOTIFY,
  '__module__' : 'genshin.packet.proto.ChallengeRecordNotify_pb2'
  # @@protoc_insertion_point(class_scope:ChallengeRecordNotify)
  })
_sym_db.RegisterMessage(ChallengeRecordNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CHALLENGERECORDNOTIFY._serialized_start=96
  _CHALLENGERECORDNOTIFY._serialized_end=186
# @@protoc_insertion_point(module_scope)
