# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PersonalLineAllDataRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import LockedPersonallineData_pb2 as genshin_dot_packet_dot_proto_dot_LockedPersonallineData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/PersonalLineAllDataRsp.proto\x1a\x31genshin/packet/proto/LockedPersonallineData.proto\"\xf9\x01\n\x16PersonalLineAllDataRsp\x12%\n\x1d\x63ur_finished_daily_task_count\x18\x05 \x01(\r\x12*\n\"can_be_unlocked_personal_line_list\x18\r \x03(\r\x12\x0f\n\x07retcode\x18\x0f \x01(\x05\x12\"\n\x1aongoing_personal_line_list\x18\x08 \x03(\r\x12\x1b\n\x13legendary_key_count\x18\x0b \x01(\r\x12:\n\x19locked_personal_line_list\x18\n \x03(\x0b\x32\x17.LockedPersonallineDataB\x16\n\x14org.sorapointa.protob\x06proto3')



_PERSONALLINEALLDATARSP = DESCRIPTOR.message_types_by_name['PersonalLineAllDataRsp']
PersonalLineAllDataRsp = _reflection.GeneratedProtocolMessageType('PersonalLineAllDataRsp', (_message.Message,), {
  'DESCRIPTOR' : _PERSONALLINEALLDATARSP,
  '__module__' : 'genshin.packet.proto.PersonalLineAllDataRsp_pb2'
  # @@protoc_insertion_point(class_scope:PersonalLineAllDataRsp)
  })
_sym_db.RegisterMessage(PersonalLineAllDataRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PERSONALLINEALLDATARSP._serialized_start=105
  _PERSONALLINEALLDATARSP._serialized_end=354
# @@protoc_insertion_point(module_scope)
