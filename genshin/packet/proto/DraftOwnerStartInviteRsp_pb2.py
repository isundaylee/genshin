# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/DraftOwnerStartInviteRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import DraftInviteFailInfo_pb2 as genshin_dot_packet_dot_proto_dot_DraftInviteFailInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/DraftOwnerStartInviteRsp.proto\x1a.genshin/packet/proto/DraftInviteFailInfo.proto\"\x85\x01\n\x18\x44raftOwnerStartInviteRsp\x12\x33\n\x15invite_fail_info_list\x18\x0f \x03(\x0b\x32\x14.DraftInviteFailInfo\x12\x0f\n\x07retcode\x18\t \x01(\x05\x12\x11\n\twrong_uid\x18\x03 \x01(\r\x12\x10\n\x08\x64raft_id\x18\x0e \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_DRAFTOWNERSTARTINVITERSP = DESCRIPTOR.message_types_by_name['DraftOwnerStartInviteRsp']
DraftOwnerStartInviteRsp = _reflection.GeneratedProtocolMessageType('DraftOwnerStartInviteRsp', (_message.Message,), {
  'DESCRIPTOR' : _DRAFTOWNERSTARTINVITERSP,
  '__module__' : 'genshin.packet.proto.DraftOwnerStartInviteRsp_pb2'
  # @@protoc_insertion_point(class_scope:DraftOwnerStartInviteRsp)
  })
_sym_db.RegisterMessage(DraftOwnerStartInviteRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _DRAFTOWNERSTARTINVITERSP._serialized_start=104
  _DRAFTOWNERSTARTINVITERSP._serialized_end=237
# @@protoc_insertion_point(module_scope)
