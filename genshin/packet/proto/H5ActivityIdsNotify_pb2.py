# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/H5ActivityIdsNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/H5ActivityIdsNotify.proto\"\xb0\x01\n\x13H5ActivityIdsNotify\x12 \n\x18\x63lient_red_dot_timestamp\x18\x01 \x01(\r\x12\x41\n\x10h_5_activity_map\x18\x0c \x03(\x0b\x32\'.H5ActivityIdsNotify.H5ActivityMapEntry\x1a\x34\n\x12H5ActivityMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_H5ACTIVITYIDSNOTIFY = DESCRIPTOR.message_types_by_name['H5ActivityIdsNotify']
_H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY = _H5ACTIVITYIDSNOTIFY.nested_types_by_name['H5ActivityMapEntry']
H5ActivityIdsNotify = _reflection.GeneratedProtocolMessageType('H5ActivityIdsNotify', (_message.Message,), {

  'H5ActivityMapEntry' : _reflection.GeneratedProtocolMessageType('H5ActivityMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY,
    '__module__' : 'genshin.packet.proto.H5ActivityIdsNotify_pb2'
    # @@protoc_insertion_point(class_scope:H5ActivityIdsNotify.H5ActivityMapEntry)
    })
  ,
  'DESCRIPTOR' : _H5ACTIVITYIDSNOTIFY,
  '__module__' : 'genshin.packet.proto.H5ActivityIdsNotify_pb2'
  # @@protoc_insertion_point(class_scope:H5ActivityIdsNotify)
  })
_sym_db.RegisterMessage(H5ActivityIdsNotify)
_sym_db.RegisterMessage(H5ActivityIdsNotify.H5ActivityMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY._options = None
  _H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY._serialized_options = b'8\001'
  _H5ACTIVITYIDSNOTIFY._serialized_start=51
  _H5ACTIVITYIDSNOTIFY._serialized_end=227
  _H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY._serialized_start=175
  _H5ACTIVITYIDSNOTIFY_H5ACTIVITYMAPENTRY._serialized_end=227
# @@protoc_insertion_point(module_scope)
