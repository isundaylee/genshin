# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MailChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import MailData_pb2 as genshin_dot_packet_dot_proto_dot_MailData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/MailChangeNotify.proto\x1a#genshin/packet/proto/MailData.proto\"J\n\x10MailChangeNotify\x12\x1c\n\tmail_list\x18\x0e \x03(\x0b\x32\t.MailData\x12\x18\n\x10\x64\x65l_mail_id_list\x18\x08 \x03(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MAILCHANGENOTIFY = DESCRIPTOR.message_types_by_name['MailChangeNotify']
MailChangeNotify = _reflection.GeneratedProtocolMessageType('MailChangeNotify', (_message.Message,), {
  'DESCRIPTOR' : _MAILCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.MailChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:MailChangeNotify)
  })
_sym_db.RegisterMessage(MailChangeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MAILCHANGENOTIFY._serialized_start=84
  _MAILCHANGENOTIFY._serialized_end=158
# @@protoc_insertion_point(module_scope)
