# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/MailItem.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EquipParam_pb2 as genshin_dot_packet_dot_proto_dot_EquipParam__pb2
from genshin.packet.proto import MaterialDeleteInfo_pb2 as genshin_dot_packet_dot_proto_dot_MaterialDeleteInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#genshin/packet/proto/MailItem.proto\x1a%genshin/packet/proto/EquipParam.proto\x1a-genshin/packet/proto/MaterialDeleteInfo.proto\"V\n\x08MailItem\x12 \n\x0b\x65quip_param\x18\x01 \x01(\x0b\x32\x0b.EquipParam\x12(\n\x0b\x64\x65lete_info\x18\x02 \x01(\x0b\x32\x13.MaterialDeleteInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_MAILITEM = DESCRIPTOR.message_types_by_name['MailItem']
MailItem = _reflection.GeneratedProtocolMessageType('MailItem', (_message.Message,), {
  'DESCRIPTOR' : _MAILITEM,
  '__module__' : 'genshin.packet.proto.MailItem_pb2'
  # @@protoc_insertion_point(class_scope:MailItem)
  })
_sym_db.RegisterMessage(MailItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _MAILITEM._serialized_start=125
  _MAILITEM._serialized_end=211
# @@protoc_insertion_point(module_scope)
