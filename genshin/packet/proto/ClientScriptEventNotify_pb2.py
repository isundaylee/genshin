# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientScriptEventNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/ClientScriptEventNotify.proto\"u\n\x17\x43lientScriptEventNotify\x12\x12\n\nparam_list\x18\t \x03(\x05\x12\x18\n\x10source_entity_id\x18\x0e \x01(\r\x12\x12\n\nevent_type\x18\n \x01(\r\x12\x18\n\x10target_entity_id\x18\r \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTSCRIPTEVENTNOTIFY = DESCRIPTOR.message_types_by_name['ClientScriptEventNotify']
ClientScriptEventNotify = _reflection.GeneratedProtocolMessageType('ClientScriptEventNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSCRIPTEVENTNOTIFY,
  '__module__' : 'genshin.packet.proto.ClientScriptEventNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientScriptEventNotify)
  })
_sym_db.RegisterMessage(ClientScriptEventNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTSCRIPTEVENTNOTIFY._serialized_start=54
  _CLIENTSCRIPTEVENTNOTIFY._serialized_end=171
# @@protoc_insertion_point(module_scope)
