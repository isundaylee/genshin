# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MonsterSummonTagNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/MonsterSummonTagNotify.proto\"\xab\x01\n\x16MonsterSummonTagNotify\x12\x41\n\x0esummon_tag_map\x18\x01 \x03(\x0b\x32).MonsterSummonTagNotify.SummonTagMapEntry\x12\x19\n\x11monster_entity_id\x18\x08 \x01(\r\x1a\x33\n\x11SummonTagMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MONSTERSUMMONTAGNOTIFY = DESCRIPTOR.message_types_by_name['MonsterSummonTagNotify']
_MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY = _MONSTERSUMMONTAGNOTIFY.nested_types_by_name['SummonTagMapEntry']
MonsterSummonTagNotify = _reflection.GeneratedProtocolMessageType('MonsterSummonTagNotify', (_message.Message,), {

  'SummonTagMapEntry' : _reflection.GeneratedProtocolMessageType('SummonTagMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY,
    '__module__' : 'genshin.packet.proto.MonsterSummonTagNotify_pb2'
    # @@protoc_insertion_point(class_scope:MonsterSummonTagNotify.SummonTagMapEntry)
    })
  ,
  'DESCRIPTOR' : _MONSTERSUMMONTAGNOTIFY,
  '__module__' : 'genshin.packet.proto.MonsterSummonTagNotify_pb2'
  # @@protoc_insertion_point(class_scope:MonsterSummonTagNotify)
  })
_sym_db.RegisterMessage(MonsterSummonTagNotify)
_sym_db.RegisterMessage(MonsterSummonTagNotify.SummonTagMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY._options = None
  _MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY._serialized_options = b'8\001'
  _MONSTERSUMMONTAGNOTIFY._serialized_start=54
  _MONSTERSUMMONTAGNOTIFY._serialized_end=225
  _MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY._serialized_start=174
  _MONSTERSUMMONTAGNOTIFY_SUMMONTAGMAPENTRY._serialized_end=225
# @@protoc_insertion_point(module_scope)
