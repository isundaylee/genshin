# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CutSceneBeginNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/CutSceneBeginNotify.proto\"B\n\x13\x43utSceneBeginNotify\x12\x13\n\x0b\x63utscene_id\x18\x0e \x01(\r\x12\x16\n\x0eis_wait_others\x18\t \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_CUTSCENEBEGINNOTIFY = DESCRIPTOR.message_types_by_name['CutSceneBeginNotify']
CutSceneBeginNotify = _reflection.GeneratedProtocolMessageType('CutSceneBeginNotify', (_message.Message,), {
  'DESCRIPTOR' : _CUTSCENEBEGINNOTIFY,
  '__module__' : 'genshin.packet.proto.CutSceneBeginNotify_pb2'
  # @@protoc_insertion_point(class_scope:CutSceneBeginNotify)
  })
_sym_db.RegisterMessage(CutSceneBeginNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _CUTSCENEBEGINNOTIFY._serialized_start=50
  _CUTSCENEBEGINNOTIFY._serialized_end=116
# @@protoc_insertion_point(module_scope)
