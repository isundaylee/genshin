# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SceneUnlockInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/SceneUnlockInfo.proto\"L\n\x0fSceneUnlockInfo\x12\x0f\n\x07sceneId\x18\x01 \x01(\r\x12\x10\n\x08isLocked\x18\x02 \x01(\x08\x12\x16\n\x0esceneTagIdList\x18\x03 \x03(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SCENEUNLOCKINFO = DESCRIPTOR.message_types_by_name['SceneUnlockInfo']
SceneUnlockInfo = _reflection.GeneratedProtocolMessageType('SceneUnlockInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENEUNLOCKINFO,
  '__module__' : 'genshin.packet.proto.SceneUnlockInfo_pb2'
  # @@protoc_insertion_point(class_scope:SceneUnlockInfo)
  })
_sym_db.RegisterMessage(SceneUnlockInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SCENEUNLOCKINFO._serialized_start=46
  _SCENEUNLOCKINFO._serialized_end=122
# @@protoc_insertion_point(module_scope)
