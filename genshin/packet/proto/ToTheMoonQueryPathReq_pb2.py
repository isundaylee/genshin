# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ToTheMoonQueryPathReq.proto
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
    'genshin/packet/proto/ToTheMoonQueryPathReq.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/ToTheMoonQueryPathReq.proto\x1a!genshin/packet/proto/Vector.proto\"\xed\x04\n\x15ToTheMoonQueryPathReq\x12\x36\n\x0b\x66ilter_type\x18\x0f \x01(\x0e\x32!.ToTheMoonQueryPathReq.FilterType\x12\x35\n\nquery_type\x18\n \x01(\x0e\x32!.ToTheMoonQueryPathReq.OptionType\x12\x13\n\x0bPMELMGPKENE\x18\x07 \x01(\x08\x12 \n\x0f\x64\x65stination_pos\x18\x01 \x01(\x0b\x32\x07.Vector\x12\x10\n\x08scene_id\x18\t \x01(\r\x12\x13\n\x0b\x66uzzy_range\x18\x08 \x01(\x05\x12\x13\n\x0b\x45\x41HHCMBPGDJ\x18\x05 \x01(\x08\x12\x13\n\x0b\x43\x43HHHAJICHB\x18\r \x03(\x05\x12\x38\n\x0c\x61star_method\x18\x03 \x01(\x0e\x32\".ToTheMoonQueryPathReq.AStarMethod\x12\x1b\n\nsource_pos\x18\x02 \x01(\x0b\x32\x07.Vector\x12\x10\n\x08query_id\x18\x0e \x01(\x05\"0\n\nOptionType\x12\x0f\n\x0bOPTION_NONE\x10\x00\x12\x11\n\rOPTION_NORMAL\x10\x01\"v\n\x0b\x41StarMethod\x12\x17\n\x13\x41StarMethod_CLASSIC\x10\x00\x12\x18\n\x14\x41StarMethod_TENDENCY\x10\x01\x12\x18\n\x14\x41StarMethod_ADAPTIVE\x10\x02\x12\x1a\n\x16\x41StarMethod_INFLECTION\x10\x03\"J\n\nFilterType\x12\x12\n\x0e\x46ilterType_ALL\x10\x00\x12\x12\n\x0e\x46ilterType_AIR\x10\x01\x12\x14\n\x10\x46ilterType_WATER\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ToTheMoonQueryPathReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_TOTHEMOONQUERYPATHREQ']._serialized_start=88
  _globals['_TOTHEMOONQUERYPATHREQ']._serialized_end=709
  _globals['_TOTHEMOONQUERYPATHREQ_OPTIONTYPE']._serialized_start=465
  _globals['_TOTHEMOONQUERYPATHREQ_OPTIONTYPE']._serialized_end=513
  _globals['_TOTHEMOONQUERYPATHREQ_ASTARMETHOD']._serialized_start=515
  _globals['_TOTHEMOONQUERYPATHREQ_ASTARMETHOD']._serialized_end=633
  _globals['_TOTHEMOONQUERYPATHREQ_FILTERTYPE']._serialized_start=635
  _globals['_TOTHEMOONQUERYPATHREQ_FILTERTYPE']._serialized_end=709
# @@protoc_insertion_point(module_scope)