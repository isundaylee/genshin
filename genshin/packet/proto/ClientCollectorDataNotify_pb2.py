# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientCollectorDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ClientCollectorData_pb2 as genshin_dot_packet_dot_proto_dot_ClientCollectorData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/ClientCollectorDataNotify.proto\x1a.genshin/packet/proto/ClientCollectorData.proto\"U\n\x19\x43lientCollectorDataNotify\x12\x38\n\x1a\x63lient_collector_data_list\x18\r \x03(\x0b\x32\x14.ClientCollectorDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTCOLLECTORDATANOTIFY = DESCRIPTOR.message_types_by_name['ClientCollectorDataNotify']
ClientCollectorDataNotify = _reflection.GeneratedProtocolMessageType('ClientCollectorDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCOLLECTORDATANOTIFY,
  '__module__' : 'genshin.packet.proto.ClientCollectorDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientCollectorDataNotify)
  })
_sym_db.RegisterMessage(ClientCollectorDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTCOLLECTORDATANOTIFY._serialized_start=104
  _CLIENTCOLLECTORDATANOTIFY._serialized_end=189
# @@protoc_insertion_point(module_scope)
