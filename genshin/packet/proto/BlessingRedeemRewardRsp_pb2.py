# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/BlessingRedeemRewardRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/BlessingRedeemRewardRsp.proto\"\x9a\x01\n\x17\x42lessingRedeemRewardRsp\x12<\n\x0bpic_num_map\x18\x0c \x03(\x0b\x32\'.BlessingRedeemRewardRsp.PicNumMapEntry\x12\x0f\n\x07retcode\x18\x0f \x01(\x05\x1a\x30\n\x0ePicNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_BLESSINGREDEEMREWARDRSP = DESCRIPTOR.message_types_by_name['BlessingRedeemRewardRsp']
_BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY = _BLESSINGREDEEMREWARDRSP.nested_types_by_name['PicNumMapEntry']
BlessingRedeemRewardRsp = _reflection.GeneratedProtocolMessageType('BlessingRedeemRewardRsp', (_message.Message,), {

  'PicNumMapEntry' : _reflection.GeneratedProtocolMessageType('PicNumMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY,
    '__module__' : 'genshin.packet.proto.BlessingRedeemRewardRsp_pb2'
    # @@protoc_insertion_point(class_scope:BlessingRedeemRewardRsp.PicNumMapEntry)
    })
  ,
  'DESCRIPTOR' : _BLESSINGREDEEMREWARDRSP,
  '__module__' : 'genshin.packet.proto.BlessingRedeemRewardRsp_pb2'
  # @@protoc_insertion_point(class_scope:BlessingRedeemRewardRsp)
  })
_sym_db.RegisterMessage(BlessingRedeemRewardRsp)
_sym_db.RegisterMessage(BlessingRedeemRewardRsp.PicNumMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY._options = None
  _BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY._serialized_options = b'8\001'
  _BLESSINGREDEEMREWARDRSP._serialized_start=55
  _BLESSINGREDEEMREWARDRSP._serialized_end=209
  _BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY._serialized_start=161
  _BLESSINGREDEEMREWARDRSP_PICNUMMAPENTRY._serialized_end=209
# @@protoc_insertion_point(module_scope)
