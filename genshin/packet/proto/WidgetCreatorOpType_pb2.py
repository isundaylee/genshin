# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/WidgetCreatorOpType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.genshin/packet/proto/WidgetCreatorOpType.proto*\x89\x01\n\x13WidgetCreatorOpType\x12\x1f\n\x1bWIDGET_CREATOR_OP_TYPE_NONE\x10\x00\x12\"\n\x1eWIDGET_CREATOR_OP_TYPE_RETRACT\x10\x01\x12-\n)WIDGET_CREATOR_OP_TYPE_RETRACT_AND_CREATE\x10\x02\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_WIDGETCREATOROPTYPE = DESCRIPTOR.enum_types_by_name['WidgetCreatorOpType']
WidgetCreatorOpType = enum_type_wrapper.EnumTypeWrapper(_WIDGETCREATOROPTYPE)
WIDGET_CREATOR_OP_TYPE_NONE = 0
WIDGET_CREATOR_OP_TYPE_RETRACT = 1
WIDGET_CREATOR_OP_TYPE_RETRACT_AND_CREATE = 2


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WIDGETCREATOROPTYPE._serialized_start=51
  _WIDGETCREATOROPTYPE._serialized_end=188
# @@protoc_insertion_point(module_scope)
