# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlossomBriefInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/BlossomBriefInfo.proto\x1a!genshin/packet/proto/Vector.proto\"\xd8\x01\n\x10\x42lossomBriefInfo\x12\x12\n\nrefresh_id\x18\r \x01(\r\x12\x11\n\treward_id\x18\x05 \x01(\r\x12\x0f\n\x07\x63ity_id\x18\n \x01(\r\x12\r\n\x05resin\x18\x0b \x01(\r\x12\r\n\x05state\x18\x07 \x01(\r\x12\x17\n\x0fis_guide_opened\x18\x01 \x01(\x08\x12\x15\n\rmonster_level\x18\x08 \x01(\r\x12\x16\n\x0e\x63ircle_camp_id\x18\x0f \x01(\r\x12\x14\n\x03pos\x18\x0c \x01(\x0b\x32\x07.Vector\x12\x10\n\x08scene_id\x18\t \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_BLOSSOMBRIEFINFO = DESCRIPTOR.message_types_by_name['BlossomBriefInfo']
BlossomBriefInfo = _reflection.GeneratedProtocolMessageType('BlossomBriefInfo', (_message.Message,), {
  'DESCRIPTOR' : _BLOSSOMBRIEFINFO,
  '__module__' : 'genshin.packet.proto.BlossomBriefInfo_pb2'
  # @@protoc_insertion_point(class_scope:BlossomBriefInfo)
  })
_sym_db.RegisterMessage(BlossomBriefInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _BLOSSOMBRIEFINFO._serialized_start=83
  _BLOSSOMBRIEFINFO._serialized_end=299
# @@protoc_insertion_point(module_scope)
