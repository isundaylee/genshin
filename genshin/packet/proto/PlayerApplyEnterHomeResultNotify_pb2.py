# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerApplyEnterHomeResultNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;genshin/packet/proto/PlayerApplyEnterHomeResultNotify.proto\"\xbf\x03\n PlayerApplyEnterHomeResultNotify\x12\x17\n\x0ftarget_nickname\x18\x07 \x01(\t\x12\x38\n\x06reason\x18\x05 \x01(\x0e\x32(.PlayerApplyEnterHomeResultNotify.Reason\x12\x12\n\ntarget_uid\x18\x0c \x01(\r\x12\x11\n\tis_agreed\x18\t \x01(\x08\"\xa0\x02\n\x06Reason\x12\x17\n\x13REASON_PLAYER_JUDGE\x10\x00\x12%\n!REASON_PLAYER_ENTER_OPTION_REFUSE\x10\x01\x12%\n!REASON_PLAYER_ENTER_OPTION_DIRECT\x10\x02\x12\x17\n\x13REASON_SYSTEM_JUDGE\x10\x03\x12\x18\n\x14REASON_HOST_IN_MATCH\x10\x04\x12&\n\"REASON_PS_PLAYER_NOT_ACCEPT_OTHERS\x10\x05\x12\x1e\n\x1aREASON_OPEN_STATE_NOT_OPEN\x10\x06\x12\x1c\n\x18REASON_HOST_IN_EDIT_MODE\x10\x07\x12\x16\n\x12REASON_PRIOR_CHECK\x10\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLAYERAPPLYENTERHOMERESULTNOTIFY = DESCRIPTOR.message_types_by_name['PlayerApplyEnterHomeResultNotify']
_PLAYERAPPLYENTERHOMERESULTNOTIFY_REASON = _PLAYERAPPLYENTERHOMERESULTNOTIFY.enum_types_by_name['Reason']
PlayerApplyEnterHomeResultNotify = _reflection.GeneratedProtocolMessageType('PlayerApplyEnterHomeResultNotify', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERAPPLYENTERHOMERESULTNOTIFY,
  '__module__' : 'genshin.packet.proto.PlayerApplyEnterHomeResultNotify_pb2'
  # @@protoc_insertion_point(class_scope:PlayerApplyEnterHomeResultNotify)
  })
_sym_db.RegisterMessage(PlayerApplyEnterHomeResultNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLAYERAPPLYENTERHOMERESULTNOTIFY._serialized_start=64
  _PLAYERAPPLYENTERHOMERESULTNOTIFY._serialized_end=511
  _PLAYERAPPLYENTERHOMERESULTNOTIFY_REASON._serialized_start=223
  _PLAYERAPPLYENTERHOMERESULTNOTIFY_REASON._serialized_end=511
# @@protoc_insertion_point(module_scope)
