# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DungeonCandidateTeamPlayerLeaveNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DungeonCandidateTeamPlayerLeaveReason_pb2 as genshin_dot_packet_dot_proto_dot_DungeonCandidateTeamPlayerLeaveReason__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@genshin/packet/proto/DungeonCandidateTeamPlayerLeaveNotify.proto\x1a@genshin/packet/proto/DungeonCandidateTeamPlayerLeaveReason.proto\"s\n%DungeonCandidateTeamPlayerLeaveNotify\x12\x36\n\x06reason\x18\x03 \x01(\x0e\x32&.DungeonCandidateTeamPlayerLeaveReason\x12\x12\n\nplayer_uid\x18\r \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_DUNGEONCANDIDATETEAMPLAYERLEAVENOTIFY = DESCRIPTOR.message_types_by_name['DungeonCandidateTeamPlayerLeaveNotify']
DungeonCandidateTeamPlayerLeaveNotify = _reflection.GeneratedProtocolMessageType('DungeonCandidateTeamPlayerLeaveNotify', (_message.Message,), {
  'DESCRIPTOR' : _DUNGEONCANDIDATETEAMPLAYERLEAVENOTIFY,
  '__module__' : 'genshin.packet.proto.DungeonCandidateTeamPlayerLeaveNotify_pb2'
  # @@protoc_insertion_point(class_scope:DungeonCandidateTeamPlayerLeaveNotify)
  })
_sym_db.RegisterMessage(DungeonCandidateTeamPlayerLeaveNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DUNGEONCANDIDATETEAMPLAYERLEAVENOTIFY._serialized_start=134
  _DUNGEONCANDIDATETEAMPLAYERLEAVENOTIFY._serialized_end=249
# @@protoc_insertion_point(module_scope)
