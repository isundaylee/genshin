# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AISnapshotInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AISnapshotEntityData_pb2 as genshin_dot_packet_dot_proto_dot_AISnapshotEntityData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/AISnapshotInfo.proto\x1a/genshin/packet/proto/AISnapshotEntityData.proto\"=\n\x0e\x41ISnapshotInfo\x12+\n\x0c\x61i_snapshots\x18\r \x03(\x0b\x32\x15.AISnapshotEntityDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_AISNAPSHOTINFO = DESCRIPTOR.message_types_by_name['AISnapshotInfo']
AISnapshotInfo = _reflection.GeneratedProtocolMessageType('AISnapshotInfo', (_message.Message,), {
  'DESCRIPTOR' : _AISNAPSHOTINFO,
  '__module__' : 'genshin.packet.proto.AISnapshotInfo_pb2'
  # @@protoc_insertion_point(class_scope:AISnapshotInfo)
  })
_sym_db.RegisterMessage(AISnapshotInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _AISNAPSHOTINFO._serialized_start=94
  _AISNAPSHOTINFO._serialized_end=155
# @@protoc_insertion_point(module_scope)
