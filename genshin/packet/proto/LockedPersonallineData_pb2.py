# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/LockedPersonallineData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/LockedPersonallineData.proto\"\xd7\x01\n\x16LockedPersonallineData\x12\x37\n\x0block_reason\x18\x02 \x01(\x0e\x32\".LockedPersonallineData.LockReason\x12\x18\n\x10personal_line_id\x18\r \x01(\r\x12\x14\n\nchapter_id\x18\x03 \x01(\rH\x00\x12\x0f\n\x05level\x18\x01 \x01(\rH\x00\":\n\nLockReason\x12\x15\n\x11LOCK_REASON_LEVEL\x10\x00\x12\x15\n\x11LOCK_REASON_QUEST\x10\x01\x42\x07\n\x05paramB\x16\n\x14org.sorapointa.protob\x06proto3')



_LOCKEDPERSONALLINEDATA = DESCRIPTOR.message_types_by_name['LockedPersonallineData']
_LOCKEDPERSONALLINEDATA_LOCKREASON = _LOCKEDPERSONALLINEDATA.enum_types_by_name['LockReason']
LockedPersonallineData = _reflection.GeneratedProtocolMessageType('LockedPersonallineData', (_message.Message,), {
  'DESCRIPTOR' : _LOCKEDPERSONALLINEDATA,
  '__module__' : 'genshin.packet.proto.LockedPersonallineData_pb2'
  # @@protoc_insertion_point(class_scope:LockedPersonallineData)
  })
_sym_db.RegisterMessage(LockedPersonallineData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _LOCKEDPERSONALLINEDATA._serialized_start=54
  _LOCKEDPERSONALLINEDATA._serialized_end=269
  _LOCKEDPERSONALLINEDATA_LOCKREASON._serialized_start=202
  _LOCKEDPERSONALLINEDATA_LOCKREASON._serialized_end=260
# @@protoc_insertion_point(module_scope)
