# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WorldDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PropValue_pb2 as genshin_dot_packet_dot_proto_dot_PropValue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/WorldDataNotify.proto\x1a$genshin/packet/proto/PropValue.proto\"\xe6\x01\n\x0fWorldDataNotify\x12:\n\x0eworld_prop_map\x18\t \x03(\x0b\x32\".WorldDataNotify.WorldPropMapEntry\x1a?\n\x11WorldPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\"V\n\x08\x44\x61taType\x12\x12\n\x0e\x44\x41TA_TYPE_NONE\x10\x00\x12\x19\n\x15\x44\x41TA_TYPE_WORLD_LEVEL\x10\x01\x12\x1b\n\x17\x44\x41TA_TYPE_IS_IN_MP_MODE\x10\x02\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_WORLDDATANOTIFY = DESCRIPTOR.message_types_by_name['WorldDataNotify']
_WORLDDATANOTIFY_WORLDPROPMAPENTRY = _WORLDDATANOTIFY.nested_types_by_name['WorldPropMapEntry']
_WORLDDATANOTIFY_DATATYPE = _WORLDDATANOTIFY.enum_types_by_name['DataType']
WorldDataNotify = _reflection.GeneratedProtocolMessageType('WorldDataNotify', (_message.Message,), {

  'WorldPropMapEntry' : _reflection.GeneratedProtocolMessageType('WorldPropMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _WORLDDATANOTIFY_WORLDPROPMAPENTRY,
    '__module__' : 'genshin.packet.proto.WorldDataNotify_pb2'
    # @@protoc_insertion_point(class_scope:WorldDataNotify.WorldPropMapEntry)
    })
  ,
  'DESCRIPTOR' : _WORLDDATANOTIFY,
  '__module__' : 'genshin.packet.proto.WorldDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:WorldDataNotify)
  })
_sym_db.RegisterMessage(WorldDataNotify)
_sym_db.RegisterMessage(WorldDataNotify.WorldPropMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._options = None
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._serialized_options = b'8\001'
  _WORLDDATANOTIFY._serialized_start=85
  _WORLDDATANOTIFY._serialized_end=315
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._serialized_start=164
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._serialized_end=227
  _WORLDDATANOTIFY_DATATYPE._serialized_start=229
  _WORLDDATANOTIFY_DATATYPE._serialized_end=315
# @@protoc_insertion_point(module_scope)
