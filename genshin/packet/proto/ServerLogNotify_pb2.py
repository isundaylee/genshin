# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ServerLogNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServerLogLevel_pb2 as genshin_dot_packet_dot_proto_dot_ServerLogLevel__pb2
from genshin.packet.proto import ServerLogType_pb2 as genshin_dot_packet_dot_proto_dot_ServerLogType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/ServerLogNotify.proto\x1a)genshin/packet/proto/ServerLogLevel.proto\x1a(genshin/packet/proto/ServerLogType.proto\"k\n\x0fServerLogNotify\x12\x12\n\nserver_log\x18\x07 \x01(\t\x12 \n\x08log_type\x18\t \x01(\x0e\x32\x0e.ServerLogType\x12\"\n\tlog_level\x18\x0f \x01(\x0e\x32\x0f.ServerLogLevelB\x16\n\x14org.sorapointa.protob\x06proto3')



_SERVERLOGNOTIFY = DESCRIPTOR.message_types_by_name['ServerLogNotify']
ServerLogNotify = _reflection.GeneratedProtocolMessageType('ServerLogNotify', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOGNOTIFY,
  '__module__' : 'genshin.packet.proto.ServerLogNotify_pb2'
  # @@protoc_insertion_point(class_scope:ServerLogNotify)
  })
_sym_db.RegisterMessage(ServerLogNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SERVERLOGNOTIFY._serialized_start=131
  _SERVERLOGNOTIFY._serialized_end=238
# @@protoc_insertion_point(module_scope)