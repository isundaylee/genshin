# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ViewCodexReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CodexTypeData_pb2 as genshin_dot_packet_dot_proto_dot_CodexTypeData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/ViewCodexReq.proto\x1a(genshin/packet/proto/CodexTypeData.proto\"6\n\x0cViewCodexReq\x12&\n\x0etype_data_list\x18\n \x03(\x0b\x32\x0e.CodexTypeDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_VIEWCODEXREQ = DESCRIPTOR.message_types_by_name['ViewCodexReq']
ViewCodexReq = _reflection.GeneratedProtocolMessageType('ViewCodexReq', (_message.Message,), {
  'DESCRIPTOR' : _VIEWCODEXREQ,
  '__module__' : 'genshin.packet.proto.ViewCodexReq_pb2'
  # @@protoc_insertion_point(class_scope:ViewCodexReq)
  })
_sym_db.RegisterMessage(ViewCodexReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _VIEWCODEXREQ._serialized_start=85
  _VIEWCODEXREQ._serialized_end=139
# @@protoc_insertion_point(module_scope)
