# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FoundationRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FoundationOpType_pb2 as genshin_dot_packet_dot_proto_dot_FoundationOpType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/FoundationRsp.proto\x1a+genshin/packet/proto/FoundationOpType.proto\"\x8c\x01\n\rFoundationRsp\x12\"\n\x07op_type\x18\r \x01(\x0e\x32\x11.FoundationOpType\x12\x18\n\x10gadget_entity_id\x18\n \x01(\r\x12\x13\n\x0b\x62uilding_id\x18\x0b \x01(\r\x12\x17\n\x0fpoint_config_id\x18\x0c \x01(\r\x12\x0f\n\x07retcode\x18\x07 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_FOUNDATIONRSP = DESCRIPTOR.message_types_by_name['FoundationRsp']
FoundationRsp = _reflection.GeneratedProtocolMessageType('FoundationRsp', (_message.Message,), {
  'DESCRIPTOR' : _FOUNDATIONRSP,
  '__module__' : 'genshin.packet.proto.FoundationRsp_pb2'
  # @@protoc_insertion_point(class_scope:FoundationRsp)
  })
_sym_db.RegisterMessage(FoundationRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FOUNDATIONRSP._serialized_start=90
  _FOUNDATIONRSP._serialized_end=230
# @@protoc_insertion_point(module_scope)
