# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RegionSearchNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RegionSearchInfo_pb2 as genshin_dot_packet_dot_proto_dot_RegionSearchInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/RegionSearchNotify.proto\x1a+genshin/packet/proto/RegionSearchInfo.proto\"P\n\x12RegionSearchNotify\x12-\n\x12region_search_list\x18\x01 \x03(\x0b\x32\x11.RegionSearchInfo\x12\x0b\n\x03uid\x18\x08 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_REGIONSEARCHNOTIFY = DESCRIPTOR.message_types_by_name['RegionSearchNotify']
RegionSearchNotify = _reflection.GeneratedProtocolMessageType('RegionSearchNotify', (_message.Message,), {
  'DESCRIPTOR' : _REGIONSEARCHNOTIFY,
  '__module__' : 'genshin.packet.proto.RegionSearchNotify_pb2'
  # @@protoc_insertion_point(class_scope:RegionSearchNotify)
  })
_sym_db.RegisterMessage(RegionSearchNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _REGIONSEARCHNOTIFY._serialized_start=94
  _REGIONSEARCHNOTIFY._serialized_end=174
# @@protoc_insertion_point(module_scope)