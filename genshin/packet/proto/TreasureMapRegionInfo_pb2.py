# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TreasureMapRegionInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/TreasureMapRegionInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\xec\x01\n\x15TreasureMapRegionInfo\x12\x12\n\nstart_time\x18\x06 \x01(\r\x12\x18\n\x10\x63urrent_progress\x18\x0b \x01(\r\x12\x17\n\x0fis_done_mp_spot\x18\x03 \x01(\x08\x12\x10\n\x08scene_id\x18\x02 \x01(\r\x12\x13\n\x0bgoal_points\x18\x0c \x01(\r\x12\x17\n\x0fis_find_mp_spot\x18\x04 \x01(\x08\x12\x15\n\rregion_radius\x18\x01 \x01(\r\x12\"\n\x11region_center_pos\x18\t \x01(\x0b\x32\x07.Vector\x12\x11\n\tregion_id\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TREASUREMAPREGIONINFO = DESCRIPTOR.message_types_by_name['TreasureMapRegionInfo']
TreasureMapRegionInfo = _reflection.GeneratedProtocolMessageType('TreasureMapRegionInfo', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREMAPREGIONINFO,
  '__module__' : 'genshin.packet.proto.TreasureMapRegionInfo_pb2'
  # @@protoc_insertion_point(class_scope:TreasureMapRegionInfo)
  })
_sym_db.RegisterMessage(TreasureMapRegionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TREASUREMAPREGIONINFO._serialized_start=88
  _TREASUREMAPREGIONINFO._serialized_end=324
# @@protoc_insertion_point(module_scope)