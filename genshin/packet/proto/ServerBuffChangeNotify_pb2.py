# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ServerBuffChangeNotify.proto
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
    'genshin/packet/proto/ServerBuffChangeNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServerBuff_pb2 as genshin_dot_packet_dot_proto_dot_ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/ServerBuffChangeNotify.proto\x1a%genshin/packet/proto/ServerBuff.proto\"\xcc\x02\n\x16ServerBuffChangeNotify\x12\x16\n\x0e\x65ntity_id_list\x18\x01 \x03(\r\x12%\n\x10server_buff_list\x18\x02 \x03(\x0b\x32\x0b.ServerBuff\x12\x18\n\x10is_creature_buff\x18\x03 \x01(\x08\x12\x18\n\x10\x61vatar_guid_list\x18\x0b \x03(\x04\x12M\n\x17server_buff_change_type\x18\x0e \x01(\x0e\x32,.ServerBuffChangeNotify.ServerBuffChangeType\"p\n\x14ServerBuffChangeType\x12+\n\'SERVER_BUFF_CHANGE_TYPE_ADD_SERVER_BUFF\x10\x00\x12+\n\'SERVER_BUFF_CHANGE_TYPE_DEL_SERVER_BUFF\x10\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ServerBuffChangeNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_SERVERBUFFCHANGENOTIFY']._serialized_start=93
  _globals['_SERVERBUFFCHANGENOTIFY']._serialized_end=425
  _globals['_SERVERBUFFCHANGENOTIFY_SERVERBUFFCHANGETYPE']._serialized_start=313
  _globals['_SERVERBUFFCHANGENOTIFY_SERVERBUFFCHANGETYPE']._serialized_end=425
# @@protoc_insertion_point(module_scope)
