# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/TowerLevelEndNotify.proto
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
    'genshin/packet/proto/TowerLevelEndNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/TowerLevelEndNotify.proto\x1a$genshin/packet/proto/ItemParam.proto\"\xbb\x02\n\x13TowerLevelEndNotify\x12$\n\x10reward_item_list\x18\x01 \x03(\x0b\x32\n.ItemParam\x12\x15\n\rnext_floor_id\x18\x03 \x01(\r\x12\x1f\n\x17\x66inished_star_cond_list\x18\x08 \x03(\r\x12\x16\n\x0e\x63ontinue_state\x18\x0b \x01(\r\x12\x12\n\nis_success\x18\x0c \x01(\x08\"\x99\x01\n\x11\x43ontinueStateType\x12(\n$CONTINUE_STATE_TYPE_CAN_NOT_CONTINUE\x10\x00\x12,\n(CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_LEVEL\x10\x01\x12,\n(CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_FLOOR\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.TowerLevelEndNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_TOWERLEVELENDNOTIFY']._serialized_start=89
  _globals['_TOWERLEVELENDNOTIFY']._serialized_end=404
  _globals['_TOWERLEVELENDNOTIFY_CONTINUESTATETYPE']._serialized_start=251
  _globals['_TOWERLEVELENDNOTIFY_CONTINUESTATETYPE']._serialized_end=404
# @@protoc_insertion_point(module_scope)
