# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlitzRushActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BlitzRushStage_pb2 as genshin_dot_packet_dot_proto_dot_BlitzRushStage__pb2
from genshin.packet.proto import ParkourLevelInfo_pb2 as genshin_dot_packet_dot_proto_dot_ParkourLevelInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6genshin/packet/proto/BlitzRushActivityDetailInfo.proto\x1a)genshin/packet/proto/BlitzRushStage.proto\x1a+genshin/packet/proto/ParkourLevelInfo.proto\"\xad\x01\n\x1b\x42litzRushActivityDetailInfo\x12#\n\nstage_list\x18\n \x03(\x0b\x32\x0f.BlitzRushStage\x12\x1a\n\x12\x63ontent_close_time\x18\x0e \x01(\r\x12\x19\n\x11is_content_closed\x18\x02 \x01(\x08\x12\x32\n\x17parkour_level_info_list\x18\x06 \x03(\x0b\x32\x11.ParkourLevelInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_BLITZRUSHACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['BlitzRushActivityDetailInfo']
BlitzRushActivityDetailInfo = _reflection.GeneratedProtocolMessageType('BlitzRushActivityDetailInfo', (_message.Message,), {
  'DESCRIPTOR' : _BLITZRUSHACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.BlitzRushActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:BlitzRushActivityDetailInfo)
  })
_sym_db.RegisterMessage(BlitzRushActivityDetailInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BLITZRUSHACTIVITYDETAILINFO._serialized_start=147
  _BLITZRUSHACTIVITYDETAILINFO._serialized_end=320
# @@protoc_insertion_point(module_scope)
