# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MarkMapReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MapMarkPoint_pb2 as genshin_dot_packet_dot_proto_dot_MapMarkPoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/MarkMapReq.proto\x1a\'genshin/packet/proto/MapMarkPoint.proto\"\xc1\x01\n\nMarkMapReq\x12\x1b\n\x04mark\x18\x08 \x01(\x0b\x32\r.MapMarkPoint\x12\x1a\n\x03old\x18\x06 \x01(\x0b\x32\r.MapMarkPoint\x12!\n\x02op\x18\t \x01(\x0e\x32\x15.MarkMapReq.Operation\"W\n\tOperation\x12\x11\n\rOPERATION_ADD\x10\x00\x12\x11\n\rOPERATION_MOD\x10\x01\x12\x11\n\rOPERATION_DEL\x10\x02\x12\x11\n\rOPERATION_GET\x10\x03\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MARKMAPREQ = DESCRIPTOR.message_types_by_name['MarkMapReq']
_MARKMAPREQ_OPERATION = _MARKMAPREQ.enum_types_by_name['Operation']
MarkMapReq = _reflection.GeneratedProtocolMessageType('MarkMapReq', (_message.Message,), {
  'DESCRIPTOR' : _MARKMAPREQ,
  '__module__' : 'genshin.packet.proto.MarkMapReq_pb2'
  # @@protoc_insertion_point(class_scope:MarkMapReq)
  })
_sym_db.RegisterMessage(MarkMapReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MARKMAPREQ._serialized_start=83
  _MARKMAPREQ._serialized_end=276
  _MARKMAPREQ_OPERATION._serialized_start=189
  _MARKMAPREQ_OPERATION._serialized_end=276
# @@protoc_insertion_point(module_scope)
