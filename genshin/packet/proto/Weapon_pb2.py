# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Weapon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!genshin/packet/proto/Weapon.proto\"\x96\x01\n\x06Weapon\x12\r\n\x05level\x18\x01 \x01(\r\x12\x0b\n\x03\x65xp\x18\x02 \x01(\r\x12\x15\n\rpromote_level\x18\x03 \x01(\r\x12(\n\taffix_map\x18\x04 \x03(\x0b\x32\x15.Weapon.AffixMapEntry\x1a/\n\rAffixMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_WEAPON = DESCRIPTOR.message_types_by_name['Weapon']
_WEAPON_AFFIXMAPENTRY = _WEAPON.nested_types_by_name['AffixMapEntry']
Weapon = _reflection.GeneratedProtocolMessageType('Weapon', (_message.Message,), {

  'AffixMapEntry' : _reflection.GeneratedProtocolMessageType('AffixMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _WEAPON_AFFIXMAPENTRY,
    '__module__' : 'genshin.packet.proto.Weapon_pb2'
    # @@protoc_insertion_point(class_scope:Weapon.AffixMapEntry)
    })
  ,
  'DESCRIPTOR' : _WEAPON,
  '__module__' : 'genshin.packet.proto.Weapon_pb2'
  # @@protoc_insertion_point(class_scope:Weapon)
  })
_sym_db.RegisterMessage(Weapon)
_sym_db.RegisterMessage(Weapon.AffixMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WEAPON_AFFIXMAPENTRY._options = None
  _WEAPON_AFFIXMAPENTRY._serialized_options = b'8\001'
  _WEAPON._serialized_start=38
  _WEAPON._serialized_end=188
  _WEAPON_AFFIXMAPENTRY._serialized_start=141
  _WEAPON_AFFIXMAPENTRY._serialized_end=188
# @@protoc_insertion_point(module_scope)
