# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/AvatarSkillDepotChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/AvatarSkillDepotChangeNotify.proto\"\xd2\x03\n\x1c\x41vatarSkillDepotChangeNotify\x12\x16\n\x0eskill_depot_id\x18\x0f \x01(\r\x12_\n\x1bproud_skill_extra_level_map\x18\x0e \x03(\x0b\x32:.AvatarSkillDepotChangeNotify.ProudSkillExtraLevelMapEntry\x12\x16\n\x0etalent_id_list\x18\t \x03(\r\x12\x18\n\x10proud_skill_list\x18\x04 \x03(\r\x12\x1e\n\x16\x63ore_proud_skill_level\x18\x02 \x01(\r\x12\x11\n\tentity_id\x18\x07 \x01(\r\x12\x13\n\x0b\x61vatar_guid\x18\x0c \x01(\x04\x12I\n\x0fskill_level_map\x18\x03 \x03(\x0b\x32\x30.AvatarSkillDepotChangeNotify.SkillLevelMapEntry\x1a>\n\x1cProudSkillExtraLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x34\n\x12SkillLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_AVATARSKILLDEPOTCHANGENOTIFY = DESCRIPTOR.message_types_by_name['AvatarSkillDepotChangeNotify']
_AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY = _AVATARSKILLDEPOTCHANGENOTIFY.nested_types_by_name['ProudSkillExtraLevelMapEntry']
_AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY = _AVATARSKILLDEPOTCHANGENOTIFY.nested_types_by_name['SkillLevelMapEntry']
AvatarSkillDepotChangeNotify = _reflection.GeneratedProtocolMessageType('AvatarSkillDepotChangeNotify', (_message.Message,), {

  'ProudSkillExtraLevelMapEntry' : _reflection.GeneratedProtocolMessageType('ProudSkillExtraLevelMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarSkillDepotChangeNotify_pb2'
    # @@protoc_insertion_point(class_scope:AvatarSkillDepotChangeNotify.ProudSkillExtraLevelMapEntry)
    })
  ,

  'SkillLevelMapEntry' : _reflection.GeneratedProtocolMessageType('SkillLevelMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY,
    '__module__' : 'genshin.packet.proto.AvatarSkillDepotChangeNotify_pb2'
    # @@protoc_insertion_point(class_scope:AvatarSkillDepotChangeNotify.SkillLevelMapEntry)
    })
  ,
  'DESCRIPTOR' : _AVATARSKILLDEPOTCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.AvatarSkillDepotChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:AvatarSkillDepotChangeNotify)
  })
_sym_db.RegisterMessage(AvatarSkillDepotChangeNotify)
_sym_db.RegisterMessage(AvatarSkillDepotChangeNotify.ProudSkillExtraLevelMapEntry)
_sym_db.RegisterMessage(AvatarSkillDepotChangeNotify.SkillLevelMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY._options = None
  _AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY._serialized_options = b'8\001'
  _AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY._options = None
  _AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY._serialized_options = b'8\001'
  _AVATARSKILLDEPOTCHANGENOTIFY._serialized_start=60
  _AVATARSKILLDEPOTCHANGENOTIFY._serialized_end=526
  _AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY._serialized_start=410
  _AVATARSKILLDEPOTCHANGENOTIFY_PROUDSKILLEXTRALEVELMAPENTRY._serialized_end=472
  _AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY._serialized_start=474
  _AVATARSKILLDEPOTCHANGENOTIFY_SKILLLEVELMAPENTRY._serialized_end=526
# @@protoc_insertion_point(module_scope)