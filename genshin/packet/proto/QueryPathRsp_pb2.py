# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QueryPathRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/QueryPathRsp.proto\x1a!genshin/packet/proto/Vector.proto\"\xe5\x01\n\x0cQueryPathRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x10\n\x08query_id\x18\x0c \x01(\x05\x12\x32\n\x0cquery_status\x18\x08 \x01(\x0e\x32\x1c.QueryPathRsp.PathStatusType\x12\x18\n\x07\x63orners\x18\x06 \x03(\x0b\x32\x07.Vector\"d\n\x0ePathStatusType\x12\x19\n\x15PATH_STATUS_TYPE_FAIL\x10\x00\x12\x19\n\x15PATH_STATUS_TYPE_SUCC\x10\x01\x12\x1c\n\x18PATH_STATUS_TYPE_PARTIAL\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_QUERYPATHRSP = DESCRIPTOR.message_types_by_name['QueryPathRsp']
_QUERYPATHRSP_PATHSTATUSTYPE = _QUERYPATHRSP.enum_types_by_name['PathStatusType']
QueryPathRsp = _reflection.GeneratedProtocolMessageType('QueryPathRsp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPATHRSP,
  '__module__' : 'genshin.packet.proto.QueryPathRsp_pb2'
  # @@protoc_insertion_point(class_scope:QueryPathRsp)
  })
_sym_db.RegisterMessage(QueryPathRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _QUERYPATHRSP._serialized_start=79
  _QUERYPATHRSP._serialized_end=308
  _QUERYPATHRSP_PATHSTATUSTYPE._serialized_start=208
  _QUERYPATHRSP_PATHSTATUSTYPE._serialized_end=308
# @@protoc_insertion_point(module_scope)
