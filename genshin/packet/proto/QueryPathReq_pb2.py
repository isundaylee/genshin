# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/QueryPathReq.proto
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
    'genshin/packet/proto/QueryPathReq.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2
from genshin.packet.proto import Vector3Int_pb2 as genshin_dot_packet_dot_proto_dot_Vector3Int__pb2
from genshin.packet.proto import QueryFilter_pb2 as genshin_dot_packet_dot_proto_dot_QueryFilter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/QueryPathReq.proto\x1a!genshin/packet/proto/Vector.proto\x1a%genshin/packet/proto/Vector3Int.proto\x1a&genshin/packet/proto/QueryFilter.proto\"\xcc\x02\n\x0cQueryPathReq\x12 \n\x0f\x64\x65stination_pos\x18\x02 \x03(\x0b\x32\x07.Vector\x12,\n\nquery_type\x18\x03 \x01(\x0e\x32\x18.QueryPathReq.OptionType\x12\x10\n\x08scene_id\x18\x04 \x01(\r\x12\x1b\n\nsource_pos\x18\x05 \x01(\x0b\x32\x07.Vector\x12 \n\x0b\x41NCGPGGGOAJ\x18\x08 \x01(\x0b\x32\x0b.Vector3Int\x12 \n\x0bIFMLKJBFKDK\x18\t \x01(\x0b\x32\x0b.Vector3Int\x12\x10\n\x08query_id\x18\x0e \x01(\x05\x12\x1c\n\x06\x66ilter\x18\x0f \x01(\x0b\x32\x0c.QueryFilter\"I\n\nOptionType\x12\x0f\n\x0bOPTION_NONE\x10\x00\x12\x11\n\rOPTION_NORMAL\x10\x01\x12\x17\n\x13OPTION_FIRST_CAN_GO\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.QueryPathReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_QUERYPATHREQ']._serialized_start=158
  _globals['_QUERYPATHREQ']._serialized_end=490
  _globals['_QUERYPATHREQ_OPTIONTYPE']._serialized_start=417
  _globals['_QUERYPATHREQ_OPTIONTYPE']._serialized_end=490
# @@protoc_insertion_point(module_scope)
