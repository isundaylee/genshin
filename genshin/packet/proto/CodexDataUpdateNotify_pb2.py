# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CodexDataUpdateNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CodexType_pb2 as genshin_dot_packet_dot_proto_dot_CodexType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/CodexDataUpdateNotify.proto\x1a$genshin/packet/proto/CodexType.proto\"_\n\x15\x43odexDataUpdateNotify\x12\n\n\x02id\x18\x08 \x01(\r\x12 \n\x18weapon_max_promote_level\x18\x0f \x01(\r\x12\x18\n\x04type\x18\x0b \x01(\x0e\x32\n.CodexTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_CODEXDATAUPDATENOTIFY = DESCRIPTOR.message_types_by_name['CodexDataUpdateNotify']
CodexDataUpdateNotify = _reflection.GeneratedProtocolMessageType('CodexDataUpdateNotify', (_message.Message,), {
  'DESCRIPTOR' : _CODEXDATAUPDATENOTIFY,
  '__module__' : 'genshin.packet.proto.CodexDataUpdateNotify_pb2'
  # @@protoc_insertion_point(class_scope:CodexDataUpdateNotify)
  })
_sym_db.RegisterMessage(CodexDataUpdateNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _CODEXDATAUPDATENOTIFY._serialized_start=90
  _CODEXDATAUPDATENOTIFY._serialized_end=185
# @@protoc_insertion_point(module_scope)