# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/UseWidgetCreateGadgetReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/UseWidgetCreateGadgetReq.proto\x1a!genshin/packet/proto/Vector.proto\"[\n\x18UseWidgetCreateGadgetReq\x12\x14\n\x03pos\x18\x0f \x01(\x0b\x32\x07.Vector\x12\x14\n\x03rot\x18\x0c \x01(\x0b\x32\x07.Vector\x12\x13\n\x0bmaterial_id\x18\x04 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_USEWIDGETCREATEGADGETREQ = DESCRIPTOR.message_types_by_name['UseWidgetCreateGadgetReq']
UseWidgetCreateGadgetReq = _reflection.GeneratedProtocolMessageType('UseWidgetCreateGadgetReq', (_message.Message,), {
  'DESCRIPTOR' : _USEWIDGETCREATEGADGETREQ,
  '__module__' : 'genshin.packet.proto.UseWidgetCreateGadgetReq_pb2'
  # @@protoc_insertion_point(class_scope:UseWidgetCreateGadgetReq)
  })
_sym_db.RegisterMessage(UseWidgetCreateGadgetReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _USEWIDGETCREATEGADGETREQ._serialized_start=90
  _USEWIDGETCREATEGADGETREQ._serialized_end=181
# @@protoc_insertion_point(module_scope)
