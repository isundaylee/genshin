# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MassivePropSyncInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MassivePropParam_pb2 as genshin_dot_packet_dot_proto_dot_MassivePropParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/MassivePropSyncInfo.proto\x1a+genshin/packet/proto/MassivePropParam.proto\"G\n\x13MassivePropSyncInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12$\n\tprop_list\x18\x02 \x03(\x0b\x32\x11.MassivePropParamB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MASSIVEPROPSYNCINFO = DESCRIPTOR.message_types_by_name['MassivePropSyncInfo']
MassivePropSyncInfo = _reflection.GeneratedProtocolMessageType('MassivePropSyncInfo', (_message.Message,), {
  'DESCRIPTOR' : _MASSIVEPROPSYNCINFO,
  '__module__' : 'genshin.packet.proto.MassivePropSyncInfo_pb2'
  # @@protoc_insertion_point(class_scope:MassivePropSyncInfo)
  })
_sym_db.RegisterMessage(MassivePropSyncInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MASSIVEPROPSYNCINFO._serialized_start=95
  _MASSIVEPROPSYNCINFO._serialized_end=166
# @@protoc_insertion_point(module_scope)
