# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WidgetSlotChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import WidgetSlotData_pb2 as genshin_dot_packet_dot_proto_dot_WidgetSlotData__pb2
from genshin.packet.proto import WidgetSlotOp_pb2 as genshin_dot_packet_dot_proto_dot_WidgetSlotOp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/WidgetSlotChangeNotify.proto\x1a)genshin/packet/proto/WidgetSlotData.proto\x1a\'genshin/packet/proto/WidgetSlotOp.proto\"R\n\x16WidgetSlotChangeNotify\x12\x19\n\x02op\x18\x0b \x01(\x0e\x32\r.WidgetSlotOp\x12\x1d\n\x04slot\x18\x08 \x01(\x0b\x32\x0f.WidgetSlotDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_WIDGETSLOTCHANGENOTIFY = DESCRIPTOR.message_types_by_name['WidgetSlotChangeNotify']
WidgetSlotChangeNotify = _reflection.GeneratedProtocolMessageType('WidgetSlotChangeNotify', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETSLOTCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.WidgetSlotChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:WidgetSlotChangeNotify)
  })
_sym_db.RegisterMessage(WidgetSlotChangeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _WIDGETSLOTCHANGENOTIFY._serialized_start=137
  _WIDGETSLOTCHANGENOTIFY._serialized_end=219
# @@protoc_insertion_point(module_scope)
