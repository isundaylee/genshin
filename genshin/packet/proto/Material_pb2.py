# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/Material.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MaterialDeleteInfo_pb2 as genshin_dot_packet_dot_proto_dot_MaterialDeleteInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#genshin/packet/proto/Material.proto\x1a-genshin/packet/proto/MaterialDeleteInfo.proto\"C\n\x08Material\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12(\n\x0b\x64\x65lete_info\x18\x02 \x01(\x0b\x32\x13.MaterialDeleteInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MATERIAL = DESCRIPTOR.message_types_by_name['Material']
Material = _reflection.GeneratedProtocolMessageType('Material', (_message.Message,), {
  'DESCRIPTOR' : _MATERIAL,
  '__module__' : 'genshin.packet.proto.Material_pb2'
  # @@protoc_insertion_point(class_scope:Material)
  })
_sym_db.RegisterMessage(Material)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MATERIAL._serialized_start=86
  _MATERIAL._serialized_end=153
# @@protoc_insertion_point(module_scope)
