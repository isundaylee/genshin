# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TakeMaterialDeleteReturnReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MaterialDeleteReturnType_pb2 as genshin_dot_packet_dot_proto_dot_MaterialDeleteReturnType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/TakeMaterialDeleteReturnReq.proto\x1a\x33genshin/packet/proto/MaterialDeleteReturnType.proto\"F\n\x1bTakeMaterialDeleteReturnReq\x12\'\n\x04type\x18\x08 \x01(\x0e\x32\x19.MaterialDeleteReturnTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_TAKEMATERIALDELETERETURNREQ = DESCRIPTOR.message_types_by_name['TakeMaterialDeleteReturnReq']
TakeMaterialDeleteReturnReq = _reflection.GeneratedProtocolMessageType('TakeMaterialDeleteReturnReq', (_message.Message,), {
  'DESCRIPTOR' : _TAKEMATERIALDELETERETURNREQ,
  '__module__' : 'genshin.packet.proto.TakeMaterialDeleteReturnReq_pb2'
  # @@protoc_insertion_point(class_scope:TakeMaterialDeleteReturnReq)
  })
_sym_db.RegisterMessage(TakeMaterialDeleteReturnReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TAKEMATERIALDELETERETURNREQ._serialized_start=111
  _TAKEMATERIALDELETERETURNREQ._serialized_end=181
# @@protoc_insertion_point(module_scope)