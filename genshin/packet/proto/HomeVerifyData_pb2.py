# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomeVerifyData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomeSceneArrangementMuipData_pb2 as genshin_dot_packet_dot_proto_dot_HomeSceneArrangementMuipData__pb2
from genshin.packet.proto import HomeVerifySceneData_pb2 as genshin_dot_packet_dot_proto_dot_HomeVerifySceneData__pb2
from genshin.packet.proto import LanguageType_pb2 as genshin_dot_packet_dot_proto_dot_LanguageType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/HomeVerifyData.proto\x1a\x37genshin/packet/proto/HomeSceneArrangementMuipData.proto\x1a.genshin/packet/proto/HomeVerifySceneData.proto\x1a\'genshin/packet/proto/LanguageType.proto\"\xee\x01\n\x0eHomeVerifyData\x12\x1b\n\x13Unk2700_OAKBDKKBFHP\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x0f \x01(\x07\x12\x0b\n\x03uid\x18\x05 \x01(\r\x12:\n\x13Unk2700_CDELDBLKLDO\x18\t \x01(\x0b\x32\x1d.HomeSceneArrangementMuipData\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\r\n\x05token\x18\x01 \x01(\t\x12\'\n\thome_info\x18\x06 \x01(\x0b\x32\x14.HomeVerifySceneData\x12\x1b\n\x04lang\x18\x08 \x01(\x0e\x32\r.LanguageTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEVERIFYDATA = DESCRIPTOR.message_types_by_name['HomeVerifyData']
HomeVerifyData = _reflection.GeneratedProtocolMessageType('HomeVerifyData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEVERIFYDATA,
  '__module__' : 'genshin.packet.proto.HomeVerifyData_pb2'
  # @@protoc_insertion_point(class_scope:HomeVerifyData)
  })
_sym_db.RegisterMessage(HomeVerifyData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEVERIFYDATA._serialized_start=192
  _HOMEVERIFYDATA._serialized_end=430
# @@protoc_insertion_point(module_scope)