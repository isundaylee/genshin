# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SeaLampFlyLampNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/SeaLampFlyLampNotify.proto\x1a!genshin/packet/proto/Vector.proto\"^\n\x14SeaLampFlyLampNotify\x12\x14\n\x03pos\x18\x0b \x01(\x0b\x32\x07.Vector\x12\x10\n\x08item_num\x18\n \x01(\r\x12\x0f\n\x07item_id\x18\x07 \x01(\r\x12\r\n\x05param\x18\x05 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SEALAMPFLYLAMPNOTIFY = DESCRIPTOR.message_types_by_name['SeaLampFlyLampNotify']
SeaLampFlyLampNotify = _reflection.GeneratedProtocolMessageType('SeaLampFlyLampNotify', (_message.Message,), {
  'DESCRIPTOR' : _SEALAMPFLYLAMPNOTIFY,
  '__module__' : 'genshin.packet.proto.SeaLampFlyLampNotify_pb2'
  # @@protoc_insertion_point(class_scope:SeaLampFlyLampNotify)
  })
_sym_db.RegisterMessage(SeaLampFlyLampNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SEALAMPFLYLAMPNOTIFY._serialized_start=86
  _SEALAMPFLYLAMPNOTIFY._serialized_end=180
# @@protoc_insertion_point(module_scope)
