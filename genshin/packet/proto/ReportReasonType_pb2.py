# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ReportReasonType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/ReportReasonType.proto*\xf0\x01\n\x10ReportReasonType\x12\x1b\n\x17REPORT_REASON_TYPE_NONE\x10\x00\x12$\n REPORT_REASON_TYPE_DECEPTIVE_ADS\x10\x01\x12\x1e\n\x1aREPORT_REASON_TYPE_ABUSING\x10\x02\x12\x1c\n\x18REPORT_REASON_TYPE_CHEAT\x10\x03\x12 \n\x1cREPORT_REASON_TYPE_POLITICAL\x10\x04\x12\x1c\n\x18REPORT_REASON_TYPE_OTHER\x10\x05\x12\x1b\n\x17REPORT_REASON_TYPE_HOME\x10\x06\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_REPORTREASONTYPE = DESCRIPTOR.enum_types_by_name['ReportReasonType']
ReportReasonType = enum_type_wrapper.EnumTypeWrapper(_REPORTREASONTYPE)
REPORT_REASON_TYPE_NONE = 0
REPORT_REASON_TYPE_DECEPTIVE_ADS = 1
REPORT_REASON_TYPE_ABUSING = 2
REPORT_REASON_TYPE_CHEAT = 3
REPORT_REASON_TYPE_POLITICAL = 4
REPORT_REASON_TYPE_OTHER = 5
REPORT_REASON_TYPE_HOME = 6


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _REPORTREASONTYPE._serialized_start=48
  _REPORTREASONTYPE._serialized_end=288
# @@protoc_insertion_point(module_scope)
