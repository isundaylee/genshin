# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlockInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$genshin/packet/proto/BlockInfo.proto\"W\n\tBlockInfo\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x61ta_version\x18\x02 \x01(\r\x12\x10\n\x08\x62in_data\x18\x03 \x01(\x0c\x12\x10\n\x08is_dirty\x18\x04 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_BLOCKINFO = DESCRIPTOR.message_types_by_name['BlockInfo']
BlockInfo = _reflection.GeneratedProtocolMessageType('BlockInfo', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKINFO,
  '__module__' : 'genshin.packet.proto.BlockInfo_pb2'
  # @@protoc_insertion_point(class_scope:BlockInfo)
  })
_sym_db.RegisterMessage(BlockInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BLOCKINFO._serialized_start=40
  _BLOCKINFO._serialized_end=127
# @@protoc_insertion_point(module_scope)
