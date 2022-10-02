# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneWeaponInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilitySyncStateInfo_pb2 as genshin_dot_packet_dot_proto_dot_AbilitySyncStateInfo__pb2
from genshin.packet.proto import EntityRendererChangedInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityRendererChangedInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SceneWeaponInfo.proto\x1a/genshin/packet/proto/AbilitySyncStateInfo.proto\x1a\x34genshin/packet/proto/EntityRendererChangedInfo.proto\"\xc8\x02\n\x0fSceneWeaponInfo\x12\x11\n\tentity_id\x18\x01 \x01(\r\x12\x11\n\tgadget_id\x18\x02 \x01(\r\x12\x0f\n\x07item_id\x18\x03 \x01(\r\x12\x0c\n\x04guid\x18\x04 \x01(\x04\x12\r\n\x05level\x18\x05 \x01(\r\x12\x15\n\rpromote_level\x18\x06 \x01(\r\x12+\n\x0c\x61\x62ility_info\x18\x07 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x31\n\taffix_map\x18\x08 \x03(\x0b\x32\x1e.SceneWeaponInfo.AffixMapEntry\x12\x39\n\x15renderer_changed_info\x18\t \x01(\x0b\x32\x1a.EntityRendererChangedInfo\x1a/\n\rAffixMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SCENEWEAPONINFO = DESCRIPTOR.message_types_by_name['SceneWeaponInfo']
_SCENEWEAPONINFO_AFFIXMAPENTRY = _SCENEWEAPONINFO.nested_types_by_name['AffixMapEntry']
SceneWeaponInfo = _reflection.GeneratedProtocolMessageType('SceneWeaponInfo', (_message.Message,), {

  'AffixMapEntry' : _reflection.GeneratedProtocolMessageType('AffixMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCENEWEAPONINFO_AFFIXMAPENTRY,
    '__module__' : 'genshin.packet.proto.SceneWeaponInfo_pb2'
    # @@protoc_insertion_point(class_scope:SceneWeaponInfo.AffixMapEntry)
    })
  ,
  'DESCRIPTOR' : _SCENEWEAPONINFO,
  '__module__' : 'genshin.packet.proto.SceneWeaponInfo_pb2'
  # @@protoc_insertion_point(class_scope:SceneWeaponInfo)
  })
_sym_db.RegisterMessage(SceneWeaponInfo)
_sym_db.RegisterMessage(SceneWeaponInfo.AffixMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SCENEWEAPONINFO_AFFIXMAPENTRY._options = None
  _SCENEWEAPONINFO_AFFIXMAPENTRY._serialized_options = b'8\001'
  _SCENEWEAPONINFO._serialized_start=150
  _SCENEWEAPONINFO._serialized_end=478
  _SCENEWEAPONINFO_AFFIXMAPENTRY._serialized_start=431
  _SCENEWEAPONINFO_AFFIXMAPENTRY._serialized_end=478
# @@protoc_insertion_point(module_scope)
