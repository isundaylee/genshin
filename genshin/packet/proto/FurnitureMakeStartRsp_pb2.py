# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FurnitureMakeStartRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FurnitureMakeSlot_pb2 as genshin_dot_packet_dot_proto_dot_FurnitureMakeSlot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/FurnitureMakeStartRsp.proto\x1a,genshin/packet/proto/FurnitureMakeSlot.proto\"Y\n\x15\x46urnitureMakeStartRsp\x12/\n\x13\x66urniture_make_slot\x18\x05 \x01(\x0b\x32\x12.FurnitureMakeSlot\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_FURNITUREMAKESTARTRSP = DESCRIPTOR.message_types_by_name['FurnitureMakeStartRsp']
FurnitureMakeStartRsp = _reflection.GeneratedProtocolMessageType('FurnitureMakeStartRsp', (_message.Message,), {
  'DESCRIPTOR' : _FURNITUREMAKESTARTRSP,
  '__module__' : 'genshin.packet.proto.FurnitureMakeStartRsp_pb2'
  # @@protoc_insertion_point(class_scope:FurnitureMakeStartRsp)
  })
_sym_db.RegisterMessage(FurnitureMakeStartRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _FURNITUREMAKESTARTRSP._serialized_start=98
  _FURNITUREMAKESTARTRSP._serialized_end=187
# @@protoc_insertion_point(module_scope)
