# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AnimatorForceSetAirMoveNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8genshin/packet/proto/AnimatorForceSetAirMoveNotify.proto\x1a&genshin/packet/proto/ForwardType.proto\"k\n\x1d\x41nimatorForceSetAirMoveNotify\x12\x11\n\tentity_id\x18\x0e \x01(\r\x12\x13\n\x0bin_air_move\x18\r \x01(\x08\x12\"\n\x0c\x66orward_type\x18\t \x01(\x0e\x32\x0c.ForwardTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_ANIMATORFORCESETAIRMOVENOTIFY = DESCRIPTOR.message_types_by_name['AnimatorForceSetAirMoveNotify']
AnimatorForceSetAirMoveNotify = _reflection.GeneratedProtocolMessageType('AnimatorForceSetAirMoveNotify', (_message.Message,), {
  'DESCRIPTOR' : _ANIMATORFORCESETAIRMOVENOTIFY,
  '__module__' : 'genshin.packet.proto.AnimatorForceSetAirMoveNotify_pb2'
  # @@protoc_insertion_point(class_scope:AnimatorForceSetAirMoveNotify)
  })
_sym_db.RegisterMessage(AnimatorForceSetAirMoveNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _ANIMATORFORCESETAIRMOVENOTIFY._serialized_start=100
  _ANIMATORFORCESETAIRMOVENOTIFY._serialized_end=207
# @@protoc_insertion_point(module_scope)
