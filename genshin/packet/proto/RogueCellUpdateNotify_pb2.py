# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/RogueCellUpdateNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RogueCellInfo_pb2 as genshin_dot_packet_dot_proto_dot_RogueCellInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/RogueCellUpdateNotify.proto\x1a(genshin/packet/proto/RogueCellInfo.proto\":\n\x15RogueCellUpdateNotify\x12!\n\tcell_info\x18\x07 \x01(\x0b\x32\x0e.RogueCellInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_ROGUECELLUPDATENOTIFY = DESCRIPTOR.message_types_by_name['RogueCellUpdateNotify']
RogueCellUpdateNotify = _reflection.GeneratedProtocolMessageType('RogueCellUpdateNotify', (_message.Message,), {
  'DESCRIPTOR' : _ROGUECELLUPDATENOTIFY,
  '__module__' : 'genshin.packet.proto.RogueCellUpdateNotify_pb2'
  # @@protoc_insertion_point(class_scope:RogueCellUpdateNotify)
  })
_sym_db.RegisterMessage(RogueCellUpdateNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ROGUECELLUPDATENOTIFY._serialized_start=94
  _ROGUECELLUPDATENOTIFY._serialized_end=152
# @@protoc_insertion_point(module_scope)
