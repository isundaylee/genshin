# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ChannelerSlabBuffInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChannelerSlabAssistInfo_pb2 as genshin_dot_packet_dot_proto_dot_ChannelerSlabAssistInfo__pb2
from genshin.packet.proto import ChannelerSlabBuffSchemeInfo_pb2 as genshin_dot_packet_dot_proto_dot_ChannelerSlabBuffSchemeInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/ChannelerSlabBuffInfo.proto\x1a\x32genshin/packet/proto/ChannelerSlabAssistInfo.proto\x1a\x36genshin/packet/proto/ChannelerSlabBuffSchemeInfo.proto\"\xdb\x01\n\x15\x43hannelerSlabBuffInfo\x12\x39\n\x13mp_buff_scheme_info\x18\x06 \x01(\x0b\x32\x1c.ChannelerSlabBuffSchemeInfo\x12\x14\n\x0c\x62uff_id_list\x18\x08 \x03(\r\x12=\n\x17single_buff_scheme_info\x18\x07 \x01(\x0b\x32\x1c.ChannelerSlabBuffSchemeInfo\x12\x32\n\x10\x61ssist_info_list\x18\x0f \x03(\x0b\x32\x18.ChannelerSlabAssistInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_CHANNELERSLABBUFFINFO = DESCRIPTOR.message_types_by_name['ChannelerSlabBuffInfo']
ChannelerSlabBuffInfo = _reflection.GeneratedProtocolMessageType('ChannelerSlabBuffInfo', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELERSLABBUFFINFO,
  '__module__' : 'genshin.packet.proto.ChannelerSlabBuffInfo_pb2'
  # @@protoc_insertion_point(class_scope:ChannelerSlabBuffInfo)
  })
_sym_db.RegisterMessage(ChannelerSlabBuffInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CHANNELERSLABBUFFINFO._serialized_start=161
  _CHANNELERSLABBUFFINFO._serialized_end=380
# @@protoc_insertion_point(module_scope)
