# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SaveMainCoopReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SaveMainCoopReq.proto\"\xa9\x02\n\x0fSaveMainCoopReq\x12:\n\x0enormal_var_map\x18\x0f \x03(\x0b\x32\".SaveMainCoopReq.NormalVarMapEntry\x12\x17\n\x0fself_confidence\x18\x02 \x01(\r\x12\x15\n\rsave_point_id\x18\x01 \x01(\r\x12\x36\n\x0ctemp_var_map\x18\x08 \x03(\x0b\x32 .SaveMainCoopReq.TempVarMapEntry\x12\n\n\x02id\x18\x03 \x01(\r\x1a\x33\n\x11NormalVarMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x31\n\x0fTempVarMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SAVEMAINCOOPREQ = DESCRIPTOR.message_types_by_name['SaveMainCoopReq']
_SAVEMAINCOOPREQ_NORMALVARMAPENTRY = _SAVEMAINCOOPREQ.nested_types_by_name['NormalVarMapEntry']
_SAVEMAINCOOPREQ_TEMPVARMAPENTRY = _SAVEMAINCOOPREQ.nested_types_by_name['TempVarMapEntry']
SaveMainCoopReq = _reflection.GeneratedProtocolMessageType('SaveMainCoopReq', (_message.Message,), {

  'NormalVarMapEntry' : _reflection.GeneratedProtocolMessageType('NormalVarMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAVEMAINCOOPREQ_NORMALVARMAPENTRY,
    '__module__' : 'genshin.packet.proto.SaveMainCoopReq_pb2'
    # @@protoc_insertion_point(class_scope:SaveMainCoopReq.NormalVarMapEntry)
    })
  ,

  'TempVarMapEntry' : _reflection.GeneratedProtocolMessageType('TempVarMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAVEMAINCOOPREQ_TEMPVARMAPENTRY,
    '__module__' : 'genshin.packet.proto.SaveMainCoopReq_pb2'
    # @@protoc_insertion_point(class_scope:SaveMainCoopReq.TempVarMapEntry)
    })
  ,
  'DESCRIPTOR' : _SAVEMAINCOOPREQ,
  '__module__' : 'genshin.packet.proto.SaveMainCoopReq_pb2'
  # @@protoc_insertion_point(class_scope:SaveMainCoopReq)
  })
_sym_db.RegisterMessage(SaveMainCoopReq)
_sym_db.RegisterMessage(SaveMainCoopReq.NormalVarMapEntry)
_sym_db.RegisterMessage(SaveMainCoopReq.TempVarMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SAVEMAINCOOPREQ_NORMALVARMAPENTRY._options = None
  _SAVEMAINCOOPREQ_NORMALVARMAPENTRY._serialized_options = b'8\001'
  _SAVEMAINCOOPREQ_TEMPVARMAPENTRY._options = None
  _SAVEMAINCOOPREQ_TEMPVARMAPENTRY._serialized_options = b'8\001'
  _SAVEMAINCOOPREQ._serialized_start=47
  _SAVEMAINCOOPREQ._serialized_end=344
  _SAVEMAINCOOPREQ_NORMALVARMAPENTRY._serialized_start=242
  _SAVEMAINCOOPREQ_NORMALVARMAPENTRY._serialized_end=293
  _SAVEMAINCOOPREQ_TEMPVARMAPENTRY._serialized_start=295
  _SAVEMAINCOOPREQ_TEMPVARMAPENTRY._serialized_end=344
# @@protoc_insertion_point(module_scope)
