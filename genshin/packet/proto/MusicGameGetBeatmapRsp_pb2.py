# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MusicGameGetBeatmapRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MusicGameGetBeatmapReqType_pb2 as genshin_dot_packet_dot_proto_dot_MusicGameGetBeatmapReqType__pb2
from genshin.packet.proto import MusicBeatmap_pb2 as genshin_dot_packet_dot_proto_dot_MusicBeatmap__pb2
from genshin.packet.proto import MusicBriefInfo_pb2 as genshin_dot_packet_dot_proto_dot_MusicBriefInfo__pb2
from genshin.packet.proto import MusicGameUnknown1Enum_pb2 as genshin_dot_packet_dot_proto_dot_MusicGameUnknown1Enum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/MusicGameGetBeatmapRsp.proto\x1a\x35genshin/packet/proto/MusicGameGetBeatmapReqType.proto\x1a\'genshin/packet/proto/MusicBeatmap.proto\x1a)genshin/packet/proto/MusicBriefInfo.proto\x1a\x30genshin/packet/proto/MusicGameUnknown1Enum.proto\"\x8d\x02\n\x16MusicGameGetBeatmapRsp\x12\x0f\n\x07retcode\x18\r \x01(\x05\x12-\n\runknown_enum1\x18\x01 \x01(\x0e\x32\x16.MusicGameUnknown1Enum\x12\x16\n\x0emusic_share_id\x18\x05 \x01(\x04\x12-\n\x08req_type\x18\x02 \x01(\x0e\x32\x1b.MusicGameGetBeatmapReqType\x12%\n\x0cmusic_record\x18\t \x01(\x0b\x32\r.MusicBeatmapH\x00\x12,\n\x10music_brief_info\x18\xb9\x07 \x01(\x0b\x32\x0f.MusicBriefInfoH\x01\x42\t\n\x07\x62\x65\x61tmapB\x0c\n\nbrief_infoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MUSICGAMEGETBEATMAPRSP = DESCRIPTOR.message_types_by_name['MusicGameGetBeatmapRsp']
MusicGameGetBeatmapRsp = _reflection.GeneratedProtocolMessageType('MusicGameGetBeatmapRsp', (_message.Message,), {
  'DESCRIPTOR' : _MUSICGAMEGETBEATMAPRSP,
  '__module__' : 'genshin.packet.proto.MusicGameGetBeatmapRsp_pb2'
  # @@protoc_insertion_point(class_scope:MusicGameGetBeatmapRsp)
  })
_sym_db.RegisterMessage(MusicGameGetBeatmapRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MUSICGAMEGETBEATMAPRSP._serialized_start=243
  _MUSICGAMEGETBEATMAPRSP._serialized_end=512
# @@protoc_insertion_point(module_scope)
