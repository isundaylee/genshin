# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/GetChatEmojiCollectionRsp.proto
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
    'genshin/packet/proto/GetChatEmojiCollectionRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChatEmojiCollectionData_pb2 as genshin_dot_packet_dot_proto_dot_ChatEmojiCollectionData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/GetChatEmojiCollectionRsp.proto\x1a\x32genshin/packet/proto/ChatEmojiCollectionData.proto\"j\n\x19GetChatEmojiCollectionRsp\x12<\n\x1a\x63hat_emoji_collection_data\x18\x03 \x01(\x0b\x32\x18.ChatEmojiCollectionData\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.GetChatEmojiCollectionRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_GETCHATEMOJICOLLECTIONRSP']._serialized_start=108
  _globals['_GETCHATEMOJICOLLECTIONRSP']._serialized_end=214
# @@protoc_insertion_point(module_scope)
