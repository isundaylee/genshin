# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GetMapAreaRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MapAreaInfo_pb2 as genshin_dot_packet_dot_proto_dot_MapAreaInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(genshin/packet/proto/GetMapAreaRsp.proto\x1a&genshin/packet/proto/MapAreaInfo.proto\"J\n\rGetMapAreaRsp\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x12(\n\x12map_area_info_list\x18\t \x03(\x0b\x32\x0c.MapAreaInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_GETMAPAREARSP = DESCRIPTOR.message_types_by_name['GetMapAreaRsp']
GetMapAreaRsp = _reflection.GeneratedProtocolMessageType('GetMapAreaRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETMAPAREARSP,
  '__module__' : 'genshin.packet.proto.GetMapAreaRsp_pb2'
  # @@protoc_insertion_point(class_scope:GetMapAreaRsp)
  })
_sym_db.RegisterMessage(GetMapAreaRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GETMAPAREARSP._serialized_start=84
  _GETMAPAREARSP._serialized_end=158
# @@protoc_insertion_point(module_scope)
