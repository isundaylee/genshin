# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EntityForceSyncRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MotionInfo_pb2 as genshin_dot_packet_dot_proto_dot_MotionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/EntityForceSyncRsp.proto\x1a%genshin/packet/proto/MotionInfo.proto\"n\n\x12\x45ntityForceSyncRsp\x12\x12\n\nscene_time\x18\x0e \x01(\r\x12\x11\n\tentity_id\x18\x06 \x01(\r\x12 \n\x0b\x66\x61il_motion\x18\x08 \x01(\x0b\x32\x0b.MotionInfo\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_ENTITYFORCESYNCRSP = DESCRIPTOR.message_types_by_name['EntityForceSyncRsp']
EntityForceSyncRsp = _reflection.GeneratedProtocolMessageType('EntityForceSyncRsp', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYFORCESYNCRSP,
  '__module__' : 'genshin.packet.proto.EntityForceSyncRsp_pb2'
  # @@protoc_insertion_point(class_scope:EntityForceSyncRsp)
  })
_sym_db.RegisterMessage(EntityForceSyncRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ENTITYFORCESYNCRSP._serialized_start=88
  _ENTITYFORCESYNCRSP._serialized_end=198
# @@protoc_insertion_point(module_scope)