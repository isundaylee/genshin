# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CheckSegmentCRCReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import SegmentCRCInfo_pb2 as genshin_dot_packet_dot_proto_dot_SegmentCRCInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/CheckSegmentCRCReq.proto\x1a)genshin/packet/proto/SegmentCRCInfo.proto\"8\n\x12\x43heckSegmentCRCReq\x12\"\n\tinfo_list\x18\x01 \x03(\x0b\x32\x0f.SegmentCRCInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_CHECKSEGMENTCRCREQ = DESCRIPTOR.message_types_by_name['CheckSegmentCRCReq']
CheckSegmentCRCReq = _reflection.GeneratedProtocolMessageType('CheckSegmentCRCReq', (_message.Message,), {
  'DESCRIPTOR' : _CHECKSEGMENTCRCREQ,
  '__module__' : 'genshin.packet.proto.CheckSegmentCRCReq_pb2'
  # @@protoc_insertion_point(class_scope:CheckSegmentCRCReq)
  })
_sym_db.RegisterMessage(CheckSegmentCRCReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CHECKSEGMENTCRCREQ._serialized_start=92
  _CHECKSEGMENTCRCREQ._serialized_end=148
# @@protoc_insertion_point(module_scope)
