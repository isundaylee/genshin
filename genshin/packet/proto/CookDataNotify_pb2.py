# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CookDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CookRecipeData_pb2 as genshin_dot_packet_dot_proto_dot_CookRecipeData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/CookDataNotify.proto\x1a)genshin/packet/proto/CookRecipeData.proto\"J\n\x0e\x43ookDataNotify\x12\r\n\x05grade\x18\x0b \x01(\r\x12)\n\x10recipe_data_list\x18\x02 \x03(\x0b\x32\x0f.CookRecipeDataB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_COOKDATANOTIFY = DESCRIPTOR.message_types_by_name['CookDataNotify']
CookDataNotify = _reflection.GeneratedProtocolMessageType('CookDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _COOKDATANOTIFY,
  '__module__' : 'genshin.packet.proto.CookDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:CookDataNotify)
  })
_sym_db.RegisterMessage(CookDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _COOKDATANOTIFY._serialized_start=88
  _COOKDATANOTIFY._serialized_end=162
# @@protoc_insertion_point(module_scope)
