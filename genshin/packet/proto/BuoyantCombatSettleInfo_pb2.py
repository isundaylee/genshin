# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BuoyantCombatSettleInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BuoyantCombatGallerySettleInfo_pb2 as genshin_dot_packet_dot_proto_dot_BuoyantCombatGallerySettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/BuoyantCombatSettleInfo.proto\x1a\x39genshin/packet/proto/BuoyantCombatGallerySettleInfo.proto\"f\n\x17\x42uoyantCombatSettleInfo\x12\x15\n\ris_new_record\x18\x01 \x01(\x08\x12\x34\n\x0bsettle_info\x18\x03 \x01(\x0b\x32\x1f.BuoyantCombatGallerySettleInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_BUOYANTCOMBATSETTLEINFO = DESCRIPTOR.message_types_by_name['BuoyantCombatSettleInfo']
BuoyantCombatSettleInfo = _reflection.GeneratedProtocolMessageType('BuoyantCombatSettleInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUOYANTCOMBATSETTLEINFO,
  '__module__' : 'genshin.packet.proto.BuoyantCombatSettleInfo_pb2'
  # @@protoc_insertion_point(class_scope:BuoyantCombatSettleInfo)
  })
_sym_db.RegisterMessage(BuoyantCombatSettleInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BUOYANTCOMBATSETTLEINFO._serialized_start=113
  _BUOYANTCOMBATSETTLEINFO._serialized_end=215
# @@protoc_insertion_point(module_scope)
