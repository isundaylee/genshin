# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/CityReputationRequestInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/CityReputationRequestInfo.proto\"\xbd\x01\n\x19\x43ityReputationRequestInfo\x12\x0f\n\x07is_open\x18\x02 \x01(\x08\x12\x41\n\x11request_info_list\x18\x01 \x03(\x0b\x32&.CityReputationRequestInfo.RequestInfo\x1aL\n\x0bRequestInfo\x12\x12\n\nrequest_id\x18\x03 \x01(\r\x12\x10\n\x08quest_id\x18\t \x01(\r\x12\x17\n\x0fis_taken_reward\x18\x06 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_CITYREPUTATIONREQUESTINFO = DESCRIPTOR.message_types_by_name['CityReputationRequestInfo']
_CITYREPUTATIONREQUESTINFO_REQUESTINFO = _CITYREPUTATIONREQUESTINFO.nested_types_by_name['RequestInfo']
CityReputationRequestInfo = _reflection.GeneratedProtocolMessageType('CityReputationRequestInfo', (_message.Message,), {

  'RequestInfo' : _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), {
    'DESCRIPTOR' : _CITYREPUTATIONREQUESTINFO_REQUESTINFO,
    '__module__' : 'genshin.packet.proto.CityReputationRequestInfo_pb2'
    # @@protoc_insertion_point(class_scope:CityReputationRequestInfo.RequestInfo)
    })
  ,
  'DESCRIPTOR' : _CITYREPUTATIONREQUESTINFO,
  '__module__' : 'genshin.packet.proto.CityReputationRequestInfo_pb2'
  # @@protoc_insertion_point(class_scope:CityReputationRequestInfo)
  })
_sym_db.RegisterMessage(CityReputationRequestInfo)
_sym_db.RegisterMessage(CityReputationRequestInfo.RequestInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CITYREPUTATIONREQUESTINFO._serialized_start=57
  _CITYREPUTATIONREQUESTINFO._serialized_end=246
  _CITYREPUTATIONREQUESTINFO_REQUESTINFO._serialized_start=170
  _CITYREPUTATIONREQUESTINFO_REQUESTINFO._serialized_end=246
# @@protoc_insertion_point(module_scope)
