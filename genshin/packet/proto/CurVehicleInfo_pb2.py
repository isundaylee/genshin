# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/CurVehicleInfo.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'genshin/packet/proto/CurVehicleInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/CurVehicleInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\x94\x01\n\x0e\x43urVehicleInfo\x12\x11\n\tentity_id\x18\x01 \x01(\r\x12\x0b\n\x03pos\x18\x02 \x01(\r\x12\x11\n\tgadget_id\x18\x03 \x01(\r\x12\x1c\n\x0bvehicle_pos\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x13\n\x0bGIICKAOFKDB\x18\x05 \x01(\r\x12\x1c\n\x0bvehicle_rot\x18\x06 \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.CurVehicleInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_CURVEHICLEINFO']._serialized_start=81
  _globals['_CURVEHICLEINFO']._serialized_end=229
# @@protoc_insertion_point(module_scope)
