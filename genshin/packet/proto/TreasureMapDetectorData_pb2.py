# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TreasureMapDetectorData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/TreasureMapDetectorData.proto\x1a!genshin/packet/proto/Vector.proto\"\x91\x01\n\x17TreasureMapDetectorData\x12\x11\n\tregion_id\x18\x04 \x01(\r\x12\x1b\n\ncenter_pos\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x1a\n\x12is_region_detected\x18\x06 \x01(\x08\x12\x1a\n\tspot_list\x18\n \x03(\x0b\x32\x07.Vector\x12\x0e\n\x06radius\x18\x0e \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TREASUREMAPDETECTORDATA = DESCRIPTOR.message_types_by_name['TreasureMapDetectorData']
TreasureMapDetectorData = _reflection.GeneratedProtocolMessageType('TreasureMapDetectorData', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREMAPDETECTORDATA,
  '__module__' : 'genshin.packet.proto.TreasureMapDetectorData_pb2'
  # @@protoc_insertion_point(class_scope:TreasureMapDetectorData)
  })
_sym_db.RegisterMessage(TreasureMapDetectorData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TREASUREMAPDETECTORDATA._serialized_start=90
  _TREASUREMAPDETECTORDATA._serialized_end=235
# @@protoc_insertion_point(module_scope)
