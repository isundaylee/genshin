# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/TakeOfferingLevelRewardRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/TakeOfferingLevelRewardRsp.proto\x1a$genshin/packet/proto/ItemParam.proto\"u\n\x1aTakeOfferingLevelRewardRsp\x12\x13\n\x0boffering_id\x18\x03 \x01(\r\x12\x12\n\ntake_level\x18\x04 \x01(\r\x12\x0f\n\x07retcode\x18\x08 \x01(\x05\x12\x1d\n\titem_list\x18\x02 \x03(\x0b\x32\n.ItemParamB\x16\n\x14org.sorapointa.protob\x06proto3')



_TAKEOFFERINGLEVELREWARDRSP = DESCRIPTOR.message_types_by_name['TakeOfferingLevelRewardRsp']
TakeOfferingLevelRewardRsp = _reflection.GeneratedProtocolMessageType('TakeOfferingLevelRewardRsp', (_message.Message,), {
  'DESCRIPTOR' : _TAKEOFFERINGLEVELREWARDRSP,
  '__module__' : 'genshin.packet.proto.TakeOfferingLevelRewardRsp_pb2'
  # @@protoc_insertion_point(class_scope:TakeOfferingLevelRewardRsp)
  })
_sym_db.RegisterMessage(TakeOfferingLevelRewardRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _TAKEOFFERINGLEVELREWARDRSP._serialized_start=95
  _TAKEOFFERINGLEVELREWARDRSP._serialized_end=212
# @@protoc_insertion_point(module_scope)
