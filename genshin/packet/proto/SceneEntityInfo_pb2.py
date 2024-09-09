# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/SceneEntityInfo.proto
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
    'genshin/packet/proto/SceneEntityInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ProtEntityType_pb2 as genshin_dot_packet_dot_proto_dot_ProtEntityType__pb2
from genshin.packet.proto import MotionInfo_pb2 as genshin_dot_packet_dot_proto_dot_MotionInfo__pb2
from genshin.packet.proto import PropPair_pb2 as genshin_dot_packet_dot_proto_dot_PropPair__pb2
from genshin.packet.proto import FightPropPair_pb2 as genshin_dot_packet_dot_proto_dot_FightPropPair__pb2
from genshin.packet.proto import AnimatorParameterValueInfoPair_pb2 as genshin_dot_packet_dot_proto_dot_AnimatorParameterValueInfoPair__pb2
from genshin.packet.proto import EntityClientData_pb2 as genshin_dot_packet_dot_proto_dot_EntityClientData__pb2
from genshin.packet.proto import EntityEnvironmentInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityEnvironmentInfo__pb2
from genshin.packet.proto import EntityAuthorityInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityAuthorityInfo__pb2
from genshin.packet.proto import ServerBuff_pb2 as genshin_dot_packet_dot_proto_dot_ServerBuff__pb2
from genshin.packet.proto import SceneAvatarInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneAvatarInfo__pb2
from genshin.packet.proto import SceneMonsterInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneMonsterInfo__pb2
from genshin.packet.proto import SceneNpcInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneNpcInfo__pb2
from genshin.packet.proto import SceneGadgetInfo_pb2 as genshin_dot_packet_dot_proto_dot_SceneGadgetInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SceneEntityInfo.proto\x1a)genshin/packet/proto/ProtEntityType.proto\x1a%genshin/packet/proto/MotionInfo.proto\x1a#genshin/packet/proto/PropPair.proto\x1a(genshin/packet/proto/FightPropPair.proto\x1a\x39genshin/packet/proto/AnimatorParameterValueInfoPair.proto\x1a+genshin/packet/proto/EntityClientData.proto\x1a\x30genshin/packet/proto/EntityEnvironmentInfo.proto\x1a.genshin/packet/proto/EntityAuthorityInfo.proto\x1a%genshin/packet/proto/ServerBuff.proto\x1a*genshin/packet/proto/SceneAvatarInfo.proto\x1a+genshin/packet/proto/SceneMonsterInfo.proto\x1a\'genshin/packet/proto/SceneNpcInfo.proto\x1a*genshin/packet/proto/SceneGadgetInfo.proto\"\xc4\x05\n\x0fSceneEntityInfo\x12$\n\x0b\x65ntity_type\x18\x01 \x01(\x0e\x32\x0f.ProtEntityType\x12\x11\n\tentity_id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12 \n\x0bmotion_info\x18\x04 \x01(\x0b\x32\x0b.MotionInfo\x12\x1c\n\tprop_list\x18\x05 \x03(\x0b\x32\t.PropPair\x12\'\n\x0f\x66ight_prop_list\x18\x06 \x03(\x0b\x32\x0e.FightPropPair\x12\x12\n\nlife_state\x18\x07 \x01(\r\x12;\n\x12\x61nimator_para_list\x18\t \x03(\x0b\x32\x1f.AnimatorParameterValueInfoPair\x12\x1f\n\x17last_move_scene_time_ms\x18\x11 \x01(\r\x12\x1e\n\x16last_move_reliable_seq\x18\x12 \x01(\r\x12-\n\x12\x65ntity_client_data\x18\x13 \x01(\x0b\x32\x11.EntityClientData\x12<\n\x1c\x65ntity_environment_info_list\x18\x14 \x03(\x0b\x32\x16.EntityEnvironmentInfo\x12\x33\n\x15\x65ntity_authority_info\x18\x15 \x01(\x0b\x32\x14.EntityAuthorityInfo\x12\x10\n\x08tag_list\x18\x16 \x03(\t\x12%\n\x10server_buff_list\x18\x17 \x03(\x0b\x32\x0b.ServerBuff\x12\"\n\x06\x61vatar\x18\n \x01(\x0b\x32\x10.SceneAvatarInfoH\x00\x12$\n\x07monster\x18\x0b \x01(\x0b\x32\x11.SceneMonsterInfoH\x00\x12\x1c\n\x03npc\x18\x0c \x01(\x0b\x32\r.SceneNpcInfoH\x00\x12\"\n\x06gadget\x18\r \x01(\x0b\x32\x10.SceneGadgetInfoH\x00\x42\x08\n\x06\x65ntityB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.SceneEntityInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_SCENEENTITYINFO']._serialized_start=623
  _globals['_SCENEENTITYINFO']._serialized_end=1331
# @@protoc_insertion_point(module_scope)
