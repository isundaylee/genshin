# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/FireWorkData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import FireWorkInstance_pb2 as genshin_dot_packet_dot_proto_dot_FireWorkInstance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/FireWorkData.proto\x1a+genshin/packet/proto/FireWorkInstance.proto\"G\n\x0c\x46ireWorkData\x12\n\n\x02id\x18\x01 \x01(\r\x12+\n\x10\x66ireWorkInstance\x18\x02 \x03(\x0b\x32\x11.FireWorkInstanceB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_FIREWORKDATA = DESCRIPTOR.message_types_by_name['FireWorkData']
FireWorkData = _reflection.GeneratedProtocolMessageType('FireWorkData', (_message.Message,), {
  'DESCRIPTOR' : _FIREWORKDATA,
  '__module__' : 'genshin.packet.proto.FireWorkData_pb2'
  # @@protoc_insertion_point(class_scope:FireWorkData)
  })
_sym_db.RegisterMessage(FireWorkData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _FIREWORKDATA._serialized_start=88
  _FIREWORKDATA._serialized_end=159
# @@protoc_insertion_point(module_scope)