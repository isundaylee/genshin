# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeFurnitureSuiteData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/HomeFurnitureSuiteData.proto\x1a!genshin/packet/proto/Vector.proto\"\x94\x01\n\x16HomeFurnitureSuiteData\x12\x17\n\x0fis_allow_summon\x18\n \x01(\x08\x12\x10\n\x08suite_id\x18\x06 \x01(\r\x12\x1a\n\tspawn_pos\x18\x08 \x01(\x0b\x32\x07.Vector\x12\x0c\n\x04guid\x18\r \x01(\r\x12%\n\x1dincluded_furniture_index_list\x18\x01 \x03(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_HOMEFURNITURESUITEDATA = DESCRIPTOR.message_types_by_name['HomeFurnitureSuiteData']
HomeFurnitureSuiteData = _reflection.GeneratedProtocolMessageType('HomeFurnitureSuiteData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEFURNITURESUITEDATA,
  '__module__' : 'genshin.packet.proto.HomeFurnitureSuiteData_pb2'
  # @@protoc_insertion_point(class_scope:HomeFurnitureSuiteData)
  })
_sym_db.RegisterMessage(HomeFurnitureSuiteData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _HOMEFURNITURESUITEDATA._serialized_start=89
  _HOMEFURNITURESUITEDATA._serialized_end=237
# @@protoc_insertion_point(module_scope)