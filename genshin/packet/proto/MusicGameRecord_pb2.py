# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MusicGameRecord.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/MusicGameRecord.proto\"J\n\x0fMusicGameRecord\x12\x11\n\tis_unlock\x18\t \x01(\x08\x12\x11\n\tmax_score\x18\x0b \x01(\r\x12\x11\n\tmax_combo\x18\x06 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_MUSICGAMERECORD = DESCRIPTOR.message_types_by_name['MusicGameRecord']
MusicGameRecord = _reflection.GeneratedProtocolMessageType('MusicGameRecord', (_message.Message,), {
  'DESCRIPTOR' : _MUSICGAMERECORD,
  '__module__' : 'genshin.packet.proto.MusicGameRecord_pb2'
  # @@protoc_insertion_point(class_scope:MusicGameRecord)
  })
_sym_db.RegisterMessage(MusicGameRecord)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MUSICGAMERECORD._serialized_start=46
  _MUSICGAMERECORD._serialized_end=120
# @@protoc_insertion_point(module_scope)
