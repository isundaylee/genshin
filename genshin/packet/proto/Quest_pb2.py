# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/Quest.proto
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
    'genshin/packet/proto/Quest.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import LackingResourceInfo_pb2 as genshin_dot_packet_dot_proto_dot_LackingResourceInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n genshin/packet/proto/Quest.proto\x1a.genshin/packet/proto/LackingResourceInfo.proto\"\xa9\x02\n\x05Quest\x12\x10\n\x08quest_id\x18\x01 \x01(\r\x12\r\n\x05state\x18\x02 \x01(\r\x12\x12\n\nstart_time\x18\x04 \x01(\r\x12\x11\n\tis_random\x18\x05 \x01(\x08\x12\x17\n\x0fparent_quest_id\x18\x06 \x01(\r\x12\x17\n\x0fquest_config_id\x18\x07 \x01(\r\x12\x17\n\x0fstart_game_time\x18\x08 \x01(\r\x12\x13\n\x0b\x61\x63\x63\x65pt_time\x18\t \x01(\r\x12\x1c\n\x14\x66inish_progress_list\x18\n \x03(\r\x12\x1a\n\x12\x66\x61il_progress_list\x18\x0b \x03(\r\x12\x13\n\x0bMLHFBAFCKIP\x18\x0c \x03(\r\x12)\n\x0b\x45\x42POIBHNPNH\x18\r \x01(\x0b\x32\x14.LackingResourceInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.Quest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_QUEST']._serialized_start=85
  _globals['_QUEST']._serialized_end=382
# @@protoc_insertion_point(module_scope)
