# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WidgetCoolDownNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WidgetCoolDownData_pb2 as genshin_dot_packet_dot_proto_dot_WidgetCoolDownData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/WidgetCoolDownNotify.proto\x1a-genshin/packet/proto/WidgetCoolDownData.proto\"\x87\x01\n\x14WidgetCoolDownNotify\x12\x37\n\x1anormal_cool_down_data_list\x18\x01 \x03(\x0b\x32\x13.WidgetCoolDownData\x12\x36\n\x19group_cool_down_data_list\x18\x0c \x03(\x0b\x32\x13.WidgetCoolDownDataB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_WIDGETCOOLDOWNNOTIFY = DESCRIPTOR.message_types_by_name['WidgetCoolDownNotify']
WidgetCoolDownNotify = _reflection.GeneratedProtocolMessageType('WidgetCoolDownNotify', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETCOOLDOWNNOTIFY,
  '__module__' : 'genshin.packet.proto.WidgetCoolDownNotify_pb2'
  # @@protoc_insertion_point(class_scope:WidgetCoolDownNotify)
  })
_sym_db.RegisterMessage(WidgetCoolDownNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WIDGETCOOLDOWNNOTIFY._serialized_start=99
  _WIDGETCOOLDOWNNOTIFY._serialized_end=234
# @@protoc_insertion_point(module_scope)