# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlossomBriefInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BlossomBriefInfo_pb2 as genshin_dot_packet_dot_proto_dot_BlossomBriefInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/BlossomBriefInfoNotify.proto\x1a+genshin/packet/proto/BlossomBriefInfo.proto\"D\n\x16\x42lossomBriefInfoNotify\x12*\n\x0f\x62rief_info_list\x18\x04 \x03(\x0b\x32\x11.BlossomBriefInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_BLOSSOMBRIEFINFONOTIFY = DESCRIPTOR.message_types_by_name['BlossomBriefInfoNotify']
BlossomBriefInfoNotify = _reflection.GeneratedProtocolMessageType('BlossomBriefInfoNotify', (_message.Message,), {
  'DESCRIPTOR' : _BLOSSOMBRIEFINFONOTIFY,
  '__module__' : 'genshin.packet.proto.BlossomBriefInfoNotify_pb2'
  # @@protoc_insertion_point(class_scope:BlossomBriefInfoNotify)
  })
_sym_db.RegisterMessage(BlossomBriefInfoNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BLOSSOMBRIEFINFONOTIFY._serialized_start=98
  _BLOSSOMBRIEFINFONOTIFY._serialized_end=166
# @@protoc_insertion_point(module_scope)
