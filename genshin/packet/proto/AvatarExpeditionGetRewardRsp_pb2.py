# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarExpeditionGetRewardRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AvatarExpeditionInfo_pb2 as genshin_dot_packet_dot_proto_dot_AvatarExpeditionInfo__pb2
from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/AvatarExpeditionGetRewardRsp.proto\x1a/genshin/packet/proto/AvatarExpeditionInfo.proto\x1a$genshin/packet/proto/ItemParam.proto\"\x9b\x02\n\x1c\x41vatarExpeditionGetRewardRsp\x12\'\n\x13Unk2700_HBKHOBPGCLH\x18\t \x03(\x0b\x32\n.ItemParam\x12\x1d\n\titem_list\x18\x08 \x03(\x0b\x32\n.ItemParam\x12Q\n\x13\x65xpedition_info_map\x18\x0c \x03(\x0b\x32\x34.AvatarExpeditionGetRewardRsp.ExpeditionInfoMapEntry\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x1aO\n\x16\x45xpeditionInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.AvatarExpeditionInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AVATAREXPEDITIONGETREWARDRSP = DESCRIPTOR.message_types_by_name['AvatarExpeditionGetRewardRsp']
_AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY = _AVATAREXPEDITIONGETREWARDRSP.nested_types_by_name['ExpeditionInfoMapEntry']
AvatarExpeditionGetRewardRsp = _reflection.GeneratedProtocolMessageType('AvatarExpeditionGetRewardRsp', (_message.Message,), {

  'ExpeditionInfoMapEntry' : _reflection.GeneratedProtocolMessageType('ExpeditionInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarExpeditionGetRewardRsp_pb2'
    # @@protoc_insertion_point(class_scope:AvatarExpeditionGetRewardRsp.ExpeditionInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _AVATAREXPEDITIONGETREWARDRSP,
  '__module__' : 'genshin.packet.proto.AvatarExpeditionGetRewardRsp_pb2'
  # @@protoc_insertion_point(class_scope:AvatarExpeditionGetRewardRsp)
  })
_sym_db.RegisterMessage(AvatarExpeditionGetRewardRsp)
_sym_db.RegisterMessage(AvatarExpeditionGetRewardRsp.ExpeditionInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY._options = None
  _AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY._serialized_options = b'8\001'
  _AVATAREXPEDITIONGETREWARDRSP._serialized_start=147
  _AVATAREXPEDITIONGETREWARDRSP._serialized_end=430
  _AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY._serialized_start=351
  _AVATAREXPEDITIONGETREWARDRSP_EXPEDITIONINFOMAPENTRY._serialized_end=430
# @@protoc_insertion_point(module_scope)
