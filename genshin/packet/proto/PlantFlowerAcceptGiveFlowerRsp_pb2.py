# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlantFlowerAcceptGiveFlowerRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import PlantFlowerAcceptFlowerResultInfo_pb2 as genshin_dot_packet_dot_proto_dot_PlantFlowerAcceptFlowerResultInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9genshin/packet/proto/PlantFlowerAcceptGiveFlowerRsp.proto\x1a<genshin/packet/proto/PlantFlowerAcceptFlowerResultInfo.proto\"\x8d\x01\n\x1ePlantFlowerAcceptGiveFlowerRsp\x12\x13\n\x0bschedule_id\x18\x01 \x01(\r\x12\x45\n\x19\x61\x63\x63\x65pt_flower_result_info\x18\x0f \x01(\x0b\x32\".PlantFlowerAcceptFlowerResultInfo\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PLANTFLOWERACCEPTGIVEFLOWERRSP = DESCRIPTOR.message_types_by_name['PlantFlowerAcceptGiveFlowerRsp']
PlantFlowerAcceptGiveFlowerRsp = _reflection.GeneratedProtocolMessageType('PlantFlowerAcceptGiveFlowerRsp', (_message.Message,), {
  'DESCRIPTOR' : _PLANTFLOWERACCEPTGIVEFLOWERRSP,
  '__module__' : 'genshin.packet.proto.PlantFlowerAcceptGiveFlowerRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlantFlowerAcceptGiveFlowerRsp)
  })
_sym_db.RegisterMessage(PlantFlowerAcceptGiveFlowerRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PLANTFLOWERACCEPTGIVEFLOWERRSP._serialized_start=124
  _PLANTFLOWERACCEPTGIVEFLOWERRSP._serialized_end=265
# @@protoc_insertion_point(module_scope)
