# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AvatarExpeditionGetRewardRsp.proto
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
    'genshin/packet/proto/AvatarExpeditionGetRewardRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2
from genshin.packet.proto import AvatarExpeditionInfo_pb2 as genshin_dot_packet_dot_proto_dot_AvatarExpeditionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/AvatarExpeditionGetRewardRsp.proto\x1a$genshin/packet/proto/ItemParam.proto\x1a/genshin/packet/proto/AvatarExpeditionInfo.proto\"\x97\x02\n\x1c\x41vatarExpeditionGetRewardRsp\x12#\n\x0f\x65xtra_item_list\x18\r \x03(\x0b\x32\n.ItemParam\x12Q\n\x13\x65xpedition_info_map\x18\t \x03(\x0b\x32\x34.AvatarExpeditionGetRewardRsp.ExpeditionInfoMapEntry\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x12\x1d\n\titem_list\x18\x05 \x03(\x0b\x32\n.ItemParam\x1aO\n\x16\x45xpeditionInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.AvatarExpeditionInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AvatarExpeditionGetRewardRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY']._loaded_options = None
  _globals['_AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_AVATAREXPEDITIONGETREWARDRSP']._serialized_start=147
  _globals['_AVATAREXPEDITIONGETREWARDRSP']._serialized_end=426
  _globals['_AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY']._serialized_start=347
  _globals['_AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY']._serialized_end=426
# @@protoc_insertion_point(module_scope)
