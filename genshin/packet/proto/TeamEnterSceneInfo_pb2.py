# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TeamEnterSceneInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityControlBlock_pb2 as genshin_dot_packet_dot_proto_dot_AbilityControlBlock__pb2
from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/TeamEnterSceneInfo.proto\x1a.genshin/packet/proto/AbilityControlBlock.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\"\x93\x01\n\x12TeamEnterSceneInfo\x12\x33\n\x15\x61\x62ility_control_block\x18\x07 \x01(\x0b\x32\x14.AbilityControlBlock\x12\x30\n\x11team_ability_info\x18\n \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x16\n\x0eteam_entity_id\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_TEAMENTERSCENEINFO = DESCRIPTOR.message_types_by_name['TeamEnterSceneInfo']
TeamEnterSceneInfo = _reflection.GeneratedProtocolMessageType('TeamEnterSceneInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMENTERSCENEINFO,
  '__module__' : 'genshin.packet.proto.TeamEnterSceneInfo_pb2'
  # @@protoc_insertion_point(class_scope:TeamEnterSceneInfo)
  })
_sym_db.RegisterMessage(TeamEnterSceneInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _TEAMENTERSCENEINFO._serialized_start=147
  _TEAMENTERSCENEINFO._serialized_end=294
# @@protoc_insertion_point(module_scope)
