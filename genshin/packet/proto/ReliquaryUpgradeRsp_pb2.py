# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ReliquaryUpgradeRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/ReliquaryUpgradeRsp.proto\"\xbe\x01\n\x13ReliquaryUpgradeRsp\x12\x11\n\told_level\x18\x04 \x01(\r\x12\x11\n\tcur_level\x18\r \x01(\r\x12\x1d\n\x15target_reliquary_guid\x18\t \x01(\x04\x12\x1c\n\x14\x63ur_append_prop_list\x18\x02 \x03(\r\x12\x15\n\rpower_up_rate\x18\x06 \x01(\r\x12\x1c\n\x14old_append_prop_list\x18\x0f \x03(\r\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_RELIQUARYUPGRADERSP = DESCRIPTOR.message_types_by_name['ReliquaryUpgradeRsp']
ReliquaryUpgradeRsp = _reflection.GeneratedProtocolMessageType('ReliquaryUpgradeRsp', (_message.Message,), {
  'DESCRIPTOR' : _RELIQUARYUPGRADERSP,
  '__module__' : 'genshin.packet.proto.ReliquaryUpgradeRsp_pb2'
  # @@protoc_insertion_point(class_scope:ReliquaryUpgradeRsp)
  })
_sym_db.RegisterMessage(ReliquaryUpgradeRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _RELIQUARYUPGRADERSP._serialized_start=51
  _RELIQUARYUPGRADERSP._serialized_end=241
# @@protoc_insertion_point(module_scope)
