# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ForgeQueueData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/ForgeQueueData.proto\"\xb4\x01\n\x0e\x46orgeQueueData\x12\x14\n\x0c\x66inish_count\x18\r \x01(\r\x12\x1e\n\x16total_finish_timestamp\x18\x0e \x01(\r\x12\x11\n\tavatar_id\x18\x07 \x01(\r\x12\x10\n\x08queue_id\x18\x01 \x01(\r\x12\x16\n\x0eunfinish_count\x18\n \x01(\r\x12\x1d\n\x15next_finish_timestamp\x18\x0b \x01(\r\x12\x10\n\x08\x66orge_id\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_FORGEQUEUEDATA = DESCRIPTOR.message_types_by_name['ForgeQueueData']
ForgeQueueData = _reflection.GeneratedProtocolMessageType('ForgeQueueData', (_message.Message,), {
  'DESCRIPTOR' : _FORGEQUEUEDATA,
  '__module__' : 'genshin.packet.proto.ForgeQueueData_pb2'
  # @@protoc_insertion_point(class_scope:ForgeQueueData)
  })
_sym_db.RegisterMessage(ForgeQueueData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _FORGEQUEUEDATA._serialized_start=46
  _FORGEQUEUEDATA._serialized_end=226
# @@protoc_insertion_point(module_scope)