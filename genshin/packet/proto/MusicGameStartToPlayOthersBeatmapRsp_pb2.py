# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MusicGameStartToPlayOthersBeatmapRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MusicGameUnknown1Enum_pb2 as genshin_dot_packet_dot_proto_dot_MusicGameUnknown1Enum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?genshin/packet/proto/MusicGameStartToPlayOthersBeatmapRsp.proto\x1a\x30genshin/packet/proto/MusicGameUnknown1Enum.proto\"{\n$MusicGameStartToPlayOthersBeatmapRsp\x12\x0f\n\x07retcode\x18\x02 \x01(\x05\x12-\n\runknown_enum1\x18\x0b \x01(\x0e\x32\x16.MusicGameUnknown1Enum\x12\x13\n\x0b\x41MNODOLNOIM\x18\x06 \x03(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MUSICGAMESTARTTOPLAYOTHERSBEATMAPRSP = DESCRIPTOR.message_types_by_name['MusicGameStartToPlayOthersBeatmapRsp']
MusicGameStartToPlayOthersBeatmapRsp = _reflection.GeneratedProtocolMessageType('MusicGameStartToPlayOthersBeatmapRsp', (_message.Message,), {
  'DESCRIPTOR' : _MUSICGAMESTARTTOPLAYOTHERSBEATMAPRSP,
  '__module__' : 'genshin.packet.proto.MusicGameStartToPlayOthersBeatmapRsp_pb2'
  # @@protoc_insertion_point(class_scope:MusicGameStartToPlayOthersBeatmapRsp)
  })
_sym_db.RegisterMessage(MusicGameStartToPlayOthersBeatmapRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MUSICGAMESTARTTOPLAYOTHERSBEATMAPRSP._serialized_start=117
  _MUSICGAMESTARTTOPLAYOTHERSBEATMAPRSP._serialized_end=240
# @@protoc_insertion_point(module_scope)
