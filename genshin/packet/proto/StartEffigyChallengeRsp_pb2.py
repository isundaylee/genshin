# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/StartEffigyChallengeRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/StartEffigyChallengeRsp.proto\"\x84\x01\n\x17StartEffigyChallengeRsp\x12\x19\n\x11\x63ondition_id_list\x18\x02 \x03(\r\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x12\x14\n\x0c\x63hallenge_id\x18\x0f \x01(\r\x12\x15\n\rdifficulty_id\x18\n \x01(\r\x12\x10\n\x08point_id\x18\x0c \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_STARTEFFIGYCHALLENGERSP = DESCRIPTOR.message_types_by_name['StartEffigyChallengeRsp']
StartEffigyChallengeRsp = _reflection.GeneratedProtocolMessageType('StartEffigyChallengeRsp', (_message.Message,), {
  'DESCRIPTOR' : _STARTEFFIGYCHALLENGERSP,
  '__module__' : 'genshin.packet.proto.StartEffigyChallengeRsp_pb2'
  # @@protoc_insertion_point(class_scope:StartEffigyChallengeRsp)
  })
_sym_db.RegisterMessage(StartEffigyChallengeRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _STARTEFFIGYCHALLENGERSP._serialized_start=55
  _STARTEFFIGYCHALLENGERSP._serialized_end=187
# @@protoc_insertion_point(module_scope)