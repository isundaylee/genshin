# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MaterialDeleteReturnNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MaterialDeleteReturnType_pb2 as genshin_dot_packet_dot_proto_dot_MaterialDeleteReturnType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/MaterialDeleteReturnNotify.proto\x1a\x33genshin/packet/proto/MaterialDeleteReturnType.proto\"\xcf\x02\n\x1aMaterialDeleteReturnNotify\x12G\n\x0freturn_item_map\x18\x05 \x03(\x0b\x32..MaterialDeleteReturnNotify.ReturnItemMapEntry\x12\'\n\x04type\x18\x08 \x01(\x0e\x32\x19.MaterialDeleteReturnType\x12O\n\x13\x64\x65lete_material_map\x18\x06 \x03(\x0b\x32\x32.MaterialDeleteReturnNotify.DeleteMaterialMapEntry\x1a\x34\n\x12ReturnItemMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x38\n\x16\x44\x65leteMaterialMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_MATERIALDELETERETURNNOTIFY = DESCRIPTOR.message_types_by_name['MaterialDeleteReturnNotify']
_MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY = _MATERIALDELETERETURNNOTIFY.nested_types_by_name['ReturnItemMapEntry']
_MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY = _MATERIALDELETERETURNNOTIFY.nested_types_by_name['DeleteMaterialMapEntry']
MaterialDeleteReturnNotify = _reflection.GeneratedProtocolMessageType('MaterialDeleteReturnNotify', (_message.Message,), {

  'ReturnItemMapEntry' : _reflection.GeneratedProtocolMessageType('ReturnItemMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY,
    '__module__' : 'genshin.packet.proto.MaterialDeleteReturnNotify_pb2'
    # @@protoc_insertion_point(class_scope:MaterialDeleteReturnNotify.ReturnItemMapEntry)
    })
  ,

  'DeleteMaterialMapEntry' : _reflection.GeneratedProtocolMessageType('DeleteMaterialMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY,
    '__module__' : 'genshin.packet.proto.MaterialDeleteReturnNotify_pb2'
    # @@protoc_insertion_point(class_scope:MaterialDeleteReturnNotify.DeleteMaterialMapEntry)
    })
  ,
  'DESCRIPTOR' : _MATERIALDELETERETURNNOTIFY,
  '__module__' : 'genshin.packet.proto.MaterialDeleteReturnNotify_pb2'
  # @@protoc_insertion_point(class_scope:MaterialDeleteReturnNotify)
  })
_sym_db.RegisterMessage(MaterialDeleteReturnNotify)
_sym_db.RegisterMessage(MaterialDeleteReturnNotify.ReturnItemMapEntry)
_sym_db.RegisterMessage(MaterialDeleteReturnNotify.DeleteMaterialMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY._options = None
  _MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY._serialized_options = b'8\001'
  _MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY._options = None
  _MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY._serialized_options = b'8\001'
  _MATERIALDELETERETURNNOTIFY._serialized_start=111
  _MATERIALDELETERETURNNOTIFY._serialized_end=446
  _MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY._serialized_start=336
  _MATERIALDELETERETURNNOTIFY_RETURNITEMMAPENTRY._serialized_end=388
  _MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY._serialized_start=390
  _MATERIALDELETERETURNNOTIFY_DELETEMATERIALMAPENTRY._serialized_end=446
# @@protoc_insertion_point(module_scope)
