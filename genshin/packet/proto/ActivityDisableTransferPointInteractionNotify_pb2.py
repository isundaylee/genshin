# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ActivityDisableTransferPointInteractionNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Uint32Pair_pb2 as genshin_dot_packet_dot_proto_dot_Uint32Pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgenshin/packet/proto/ActivityDisableTransferPointInteractionNotify.proto\x1a%genshin/packet/proto/Uint32Pair.proto\"j\n-ActivityDisableTransferPointInteractionNotify\x12\x12\n\nis_disable\x18\n \x01(\x08\x12%\n\x10scene_point_pair\x18\x05 \x01(\x0b\x32\x0b.Uint32PairB\x16\n\x14org.sorapointa.protob\x06proto3')



_ACTIVITYDISABLETRANSFERPOINTINTERACTIONNOTIFY = DESCRIPTOR.message_types_by_name['ActivityDisableTransferPointInteractionNotify']
ActivityDisableTransferPointInteractionNotify = _reflection.GeneratedProtocolMessageType('ActivityDisableTransferPointInteractionNotify', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYDISABLETRANSFERPOINTINTERACTIONNOTIFY,
  '__module__' : 'genshin.packet.proto.ActivityDisableTransferPointInteractionNotify_pb2'
  # @@protoc_insertion_point(class_scope:ActivityDisableTransferPointInteractionNotify)
  })
_sym_db.RegisterMessage(ActivityDisableTransferPointInteractionNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ACTIVITYDISABLETRANSFERPOINTINTERACTIONNOTIFY._serialized_start=115
  _ACTIVITYDISABLETRANSFERPOINTINTERACTIONNOTIFY._serialized_end=221
# @@protoc_insertion_point(module_scope)
