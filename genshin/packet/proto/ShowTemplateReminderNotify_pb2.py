# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ShowTemplateReminderNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5genshin/packet/proto/ShowTemplateReminderNotify.proto\"y\n\x1aShowTemplateReminderNotify\x12\x16\n\x0eparam_uid_list\x18\x03 \x03(\r\x12\x12\n\nparam_list\x18\n \x03(\x05\x12\x1c\n\x14template_reminder_id\x18\x0e \x01(\r\x12\x11\n\tis_revoke\x18\x01 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_SHOWTEMPLATEREMINDERNOTIFY = DESCRIPTOR.message_types_by_name['ShowTemplateReminderNotify']
ShowTemplateReminderNotify = _reflection.GeneratedProtocolMessageType('ShowTemplateReminderNotify', (_message.Message,), {
  'DESCRIPTOR' : _SHOWTEMPLATEREMINDERNOTIFY,
  '__module__' : 'genshin.packet.proto.ShowTemplateReminderNotify_pb2'
  # @@protoc_insertion_point(class_scope:ShowTemplateReminderNotify)
  })
_sym_db.RegisterMessage(ShowTemplateReminderNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SHOWTEMPLATEREMINDERNOTIFY._serialized_start=57
  _SHOWTEMPLATEREMINDERNOTIFY._serialized_end=178
# @@protoc_insertion_point(module_scope)
