# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeNpcData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/HomeNpcData.proto\x1a!genshin/packet/proto/Vector.proto\"l\n\x0bHomeNpcData\x12\x11\n\tavatar_id\x18\x0e \x01(\r\x12\x1a\n\tspawn_pos\x18\x0f \x01(\x0b\x32\x07.Vector\x12\x12\n\ncostume_id\x18\x03 \x01(\r\x12\x1a\n\tspawn_rot\x18\r \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_HOMENPCDATA = DESCRIPTOR.message_types_by_name['HomeNpcData']
HomeNpcData = _reflection.GeneratedProtocolMessageType('HomeNpcData', (_message.Message,), {
  'DESCRIPTOR' : _HOMENPCDATA,
  '__module__' : 'genshin.packet.proto.HomeNpcData_pb2'
  # @@protoc_insertion_point(class_scope:HomeNpcData)
  })
_sym_db.RegisterMessage(HomeNpcData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _HOMENPCDATA._serialized_start=77
  _HOMENPCDATA._serialized_end=185
# @@protoc_insertion_point(module_scope)
