# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerApplyEnterMpResultNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9genshin/packet/proto/PlayerApplyEnterMpResultNotify.proto\"\xed\x04\n\x1ePlayerApplyEnterMpResultNotify\x12\x11\n\tis_agreed\x18\x02 \x01(\x08\x12\x17\n\x0ftarget_nickname\x18\x0c \x01(\t\x12\x36\n\x06reason\x18\r \x01(\x0e\x32&.PlayerApplyEnterMpResultNotify.Reason\x12\x12\n\ntarget_uid\x18\x01 \x01(\r\"\xd2\x03\n\x06Reason\x12\x17\n\x13REASON_PLAYER_JUDGE\x10\x00\x12\x1d\n\x19REASON_SCENE_CANNOT_ENTER\x10\x01\x12!\n\x1dREASON_PLAYER_CANNOT_ENTER_MP\x10\x02\x12\x17\n\x13REASON_SYSTEM_JUDGE\x10\x03\x12\"\n\x1eREASON_ALLOW_ENTER_PLAYER_FULL\x10\x04\x12&\n\"REASON_WORLD_LEVEL_LOWER_THAN_HOST\x10\x05\x12\x18\n\x14REASON_HOST_IN_MATCH\x10\x06\x12\x1e\n\x1aREASON_PLAYER_IN_BLACKLIST\x10\x07\x12&\n\"REASON_PS_PLAYER_NOT_ACCEPT_OTHERS\x10\x08\x12\x1a\n\x16REASON_HOST_IS_BLOCKED\x10\t\x12(\n$REASON_OTHER_DATA_VERSION_NOT_LATEST\x10\n\x12\"\n\x1eREASON_DATA_VERSION_NOT_LATEST\x10\x0b\x12%\n!REASON_PLAYER_NOT_IN_PLAYER_WORLD\x10\x0c\x12\x15\n\x11REASON_MAX_PLAYER\x10\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERAPPLYENTERMPRESULTNOTIFY = DESCRIPTOR.message_types_by_name['PlayerApplyEnterMpResultNotify']
_PLAYERAPPLYENTERMPRESULTNOTIFY_REASON = _PLAYERAPPLYENTERMPRESULTNOTIFY.enum_types_by_name['Reason']
PlayerApplyEnterMpResultNotify = _reflection.GeneratedProtocolMessageType('PlayerApplyEnterMpResultNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERAPPLYENTERMPRESULTNOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerApplyEnterMpResultNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerApplyEnterMpResultNotify)
  })
_sym_db.RegisterMessage(PlayerApplyEnterMpResultNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERAPPLYENTERMPRESULTNOTIFY._serialized_start=62
  _PLAYERAPPLYENTERMPRESULTNOTIFY._serialized_end=683
  _PLAYERAPPLYENTERMPRESULTNOTIFY_REASON._serialized_start=217
  _PLAYERAPPLYENTERMPRESULTNOTIFY_REASON._serialized_end=683
# @@protoc_insertion_point(module_scope)
