# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AuthorityChange.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityAuthorityInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityAuthorityInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/AuthorityChange.proto\x1a.genshin/packet/proto/EntityAuthorityInfo.proto\"t\n\x0f\x41uthorityChange\x12\x33\n\x15\x65ntity_authority_info\x18\x05 \x01(\x0b\x32\x14.EntityAuthorityInfo\x12\x19\n\x11\x61uthority_peer_id\x18\x03 \x01(\r\x12\x11\n\tentity_id\x18\r \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_AUTHORITYCHANGE = DESCRIPTOR.message_types_by_name['AuthorityChange']
AuthorityChange = _reflection.GeneratedProtocolMessageType('AuthorityChange', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORITYCHANGE,
  '__module__' : 'genshin.packet.proto.AuthorityChange_pb2'
  # @@protoc_insertion_point(class_scope:AuthorityChange)
  })
_sym_db.RegisterMessage(AuthorityChange)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _AUTHORITYCHANGE._serialized_start=94
  _AUTHORITYCHANGE._serialized_end=210
# @@protoc_insertion_point(module_scope)