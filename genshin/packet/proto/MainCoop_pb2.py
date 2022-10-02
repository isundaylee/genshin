# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MainCoop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#genshin/packet/proto/MainCoop.proto\"\xef\x03\n\x08MainCoop\x12\x35\n\x0fseen_ending_map\x18\r \x03(\x0b\x32\x1c.MainCoop.SeenEndingMapEntry\x12\x33\n\x0enormal_var_map\x18\x04 \x03(\x0b\x32\x1b.MainCoop.NormalVarMapEntry\x12\x17\n\x0fself_confidence\x18\x05 \x01(\r\x12\x1a\n\x12save_point_id_list\x18\x01 \x03(\r\x12 \n\x06status\x18\x06 \x01(\x0e\x32\x10.MainCoop.Status\x12/\n\x0ctemp_var_map\x18\x0b \x03(\x0b\x32\x19.MainCoop.TempVarMapEntry\x12\n\n\x02id\x18\t \x01(\r\x1a\x34\n\x12SeenEndingMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x33\n\x11NormalVarMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x31\n\x0fTempVarMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"E\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x12\n\x0eSTATUS_RUNNING\x10\x01\x12\x13\n\x0fSTATUS_FINISHED\x10\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MAINCOOP = DESCRIPTOR.message_types_by_name['MainCoop']
_MAINCOOP_SEENENDINGMAPENTRY = _MAINCOOP.nested_types_by_name['SeenEndingMapEntry']
_MAINCOOP_NORMALVARMAPENTRY = _MAINCOOP.nested_types_by_name['NormalVarMapEntry']
_MAINCOOP_TEMPVARMAPENTRY = _MAINCOOP.nested_types_by_name['TempVarMapEntry']
_MAINCOOP_STATUS = _MAINCOOP.enum_types_by_name['Status']
MainCoop = _reflection.GeneratedProtocolMessageType('MainCoop', (_message.Message,), {

  'SeenEndingMapEntry' : _reflection.GeneratedProtocolMessageType('SeenEndingMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAINCOOP_SEENENDINGMAPENTRY,
    '__module__' : 'genshin.packet.proto.MainCoop_pb2'
    # @@protoc_insertion_point(class_scope:MainCoop.SeenEndingMapEntry)
    })
  ,

  'NormalVarMapEntry' : _reflection.GeneratedProtocolMessageType('NormalVarMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAINCOOP_NORMALVARMAPENTRY,
    '__module__' : 'genshin.packet.proto.MainCoop_pb2'
    # @@protoc_insertion_point(class_scope:MainCoop.NormalVarMapEntry)
    })
  ,

  'TempVarMapEntry' : _reflection.GeneratedProtocolMessageType('TempVarMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAINCOOP_TEMPVARMAPENTRY,
    '__module__' : 'genshin.packet.proto.MainCoop_pb2'
    # @@protoc_insertion_point(class_scope:MainCoop.TempVarMapEntry)
    })
  ,
  'DESCRIPTOR' : _MAINCOOP,
  '__module__' : 'genshin.packet.proto.MainCoop_pb2'
  # @@protoc_insertion_point(class_scope:MainCoop)
  })
_sym_db.RegisterMessage(MainCoop)
_sym_db.RegisterMessage(MainCoop.SeenEndingMapEntry)
_sym_db.RegisterMessage(MainCoop.NormalVarMapEntry)
_sym_db.RegisterMessage(MainCoop.TempVarMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MAINCOOP_SEENENDINGMAPENTRY._options = None
  _MAINCOOP_SEENENDINGMAPENTRY._serialized_options = b'8\001'
  _MAINCOOP_NORMALVARMAPENTRY._options = None
  _MAINCOOP_NORMALVARMAPENTRY._serialized_options = b'8\001'
  _MAINCOOP_TEMPVARMAPENTRY._options = None
  _MAINCOOP_TEMPVARMAPENTRY._serialized_options = b'8\001'
  _MAINCOOP._serialized_start=40
  _MAINCOOP._serialized_end=535
  _MAINCOOP_SEENENDINGMAPENTRY._serialized_start=308
  _MAINCOOP_SEENENDINGMAPENTRY._serialized_end=360
  _MAINCOOP_NORMALVARMAPENTRY._serialized_start=362
  _MAINCOOP_NORMALVARMAPENTRY._serialized_end=413
  _MAINCOOP_TEMPVARMAPENTRY._serialized_start=415
  _MAINCOOP_TEMPVARMAPENTRY._serialized_end=464
  _MAINCOOP_STATUS._serialized_start=466
  _MAINCOOP_STATUS._serialized_end=535
# @@protoc_insertion_point(module_scope)
