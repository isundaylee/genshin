# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AnchorPointDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AnchorPointData_pb2 as genshin_dot_packet_dot_proto_dot_AnchorPointData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/AnchorPointDataNotify.proto\x1a*genshin/packet/proto/AnchorPointData.proto\"^\n\x15\x41nchorPointDataNotify\x12+\n\x11\x61nchor_point_list\x18\n \x03(\x0b\x32\x10.AnchorPointData\x12\x18\n\x10next_usable_time\x18\x0e \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_ANCHORPOINTDATANOTIFY = DESCRIPTOR.message_types_by_name['AnchorPointDataNotify']
AnchorPointDataNotify = _reflection.GeneratedProtocolMessageType('AnchorPointDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _ANCHORPOINTDATANOTIFY,
  '__module__' : 'genshin.packet.proto.AnchorPointDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:AnchorPointDataNotify)
  })
_sym_db.RegisterMessage(AnchorPointDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ANCHORPOINTDATANOTIFY._serialized_start=96
  _ANCHORPOINTDATANOTIFY._serialized_end=190
# @@protoc_insertion_point(module_scope)
