# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ChallengeDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/ChallengeDataNotify.proto\"R\n\x13\x43hallengeDataNotify\x12\r\n\x05value\x18\x08 \x01(\r\x12\x17\n\x0f\x63hallenge_index\x18\x02 \x01(\r\x12\x13\n\x0bparam_index\x18\t \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_CHALLENGEDATANOTIFY = DESCRIPTOR.message_types_by_name['ChallengeDataNotify']
ChallengeDataNotify = _reflection.GeneratedProtocolMessageType('ChallengeDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEDATANOTIFY,
  '__module__' : 'genshin.packet.proto.ChallengeDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:ChallengeDataNotify)
  })
_sym_db.RegisterMessage(ChallengeDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _CHALLENGEDATANOTIFY._serialized_start=50
  _CHALLENGEDATANOTIFY._serialized_end=132
# @@protoc_insertion_point(module_scope)