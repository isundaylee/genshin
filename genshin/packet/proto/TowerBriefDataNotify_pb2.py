# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TowerBriefDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/genshin/packet/proto/TowerBriefDataNotify.proto\"\xe1\x01\n\x14TowerBriefDataNotify\x12\x16\n\x0etotal_star_num\x18\x0b \x01(\r\x12\x18\n\x10last_floor_index\x18\x08 \x01(\r\x12\x1b\n\x13schedule_start_time\x18\x0f \x01(\r\x12!\n\x19next_schedule_change_time\x18\x06 \x01(\r\x12\"\n\x1ais_finished_entrance_floor\x18\x0e \x01(\x08\x12\x18\n\x10last_level_index\x18\x04 \x01(\r\x12\x19\n\x11tower_schedule_id\x18\x05 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_TOWERBRIEFDATANOTIFY = DESCRIPTOR.message_types_by_name['TowerBriefDataNotify']
TowerBriefDataNotify = _reflection.GeneratedProtocolMessageType('TowerBriefDataNotify', (_message.Message,), {
  'DESCRIPTOR' : _TOWERBRIEFDATANOTIFY,
  '__module__' : 'genshin.packet.proto.TowerBriefDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:TowerBriefDataNotify)
  })
_sym_db.RegisterMessage(TowerBriefDataNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TOWERBRIEFDATANOTIFY._serialized_start=52
  _TOWERBRIEFDATANOTIFY._serialized_end=277
# @@protoc_insertion_point(module_scope)
