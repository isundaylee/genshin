# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/ChatInfo.proto
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
    'genshin/packet/proto/ChatInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#genshin/packet/proto/ChatInfo.proto\"\xce\x02\n\x08\x43hatInfo\x12\x0f\n\x07is_read\x18\x04 \x01(\x08\x12\x0c\n\x04time\x18\x08 \x01(\r\x12\x0e\n\x06to_uid\x18\x05 \x01(\r\x12\x10\n\x08sequence\x18\x07 \x01(\r\x12\x0b\n\x03uid\x18\n \x01(\r\x12\x0e\n\x04icon\x18\x15 \x01(\rH\x00\x12\x0f\n\x04text\x18\xe5\x02 \x01(\tH\x00\x12,\n\x0bsystem_hint\x18\x9a\x07 \x01(\x0b\x32\x14.ChatInfo.SystemHintH\x00\x1a\x1a\n\nSystemHint\x12\x0c\n\x04type\x18\x07 \x01(\r\"~\n\x0eSystemHintType\x12\x1e\n\x1aSYSTEM_HINT_TYPE_CHAT_NONE\x10\x00\x12%\n!SYSTEM_HINT_TYPE_CHAT_ENTER_WORLD\x10\x01\x12%\n!SYSTEM_HINT_TYPE_CHAT_LEAVE_WORLD\x10\x02\x42\t\n\x07\x63ontentB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.ChatInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_CHATINFO']._serialized_start=40
  _globals['_CHATINFO']._serialized_end=374
  _globals['_CHATINFO_SYSTEMHINT']._serialized_start=209
  _globals['_CHATINFO_SYSTEMHINT']._serialized_end=235
  _globals['_CHATINFO_SYSTEMHINTTYPE']._serialized_start=237
  _globals['_CHATINFO_SYSTEMHINTTYPE']._serialized_end=363
# @@protoc_insertion_point(module_scope)
