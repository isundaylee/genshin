# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ServerBuffChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ServerBuff_pb2 as genshin_dot_packet_dot_proto_dot_ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/ServerBuffChangeNotify.proto\x1a%genshin/packet/proto/ServerBuff.proto\"\xcc\x02\n\x16ServerBuffChangeNotify\x12M\n\x17server_buff_change_type\x18\x07 \x01(\x0e\x32,.ServerBuffChangeNotify.ServerBuffChangeType\x12\x18\n\x10is_creature_buff\x18\n \x01(\x08\x12\x16\n\x0e\x65ntity_id_list\x18\x01 \x03(\r\x12\x18\n\x10\x61vatar_guid_list\x18\x0c \x03(\x04\x12%\n\x10server_buff_list\x18\x0b \x03(\x0b\x32\x0b.ServerBuff\"p\n\x14ServerBuffChangeType\x12+\n\'SERVER_BUFF_CHANGE_TYPE_ADD_SERVER_BUFF\x10\x00\x12+\n\'SERVER_BUFF_CHANGE_TYPE_DEL_SERVER_BUFF\x10\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_SERVERBUFFCHANGENOTIFY = DESCRIPTOR.message_types_by_name['ServerBuffChangeNotify']
_SERVERBUFFCHANGENOTIFY_SERVERBUFFCHANGETYPE = _SERVERBUFFCHANGENOTIFY.enum_types_by_name['ServerBuffChangeType']
ServerBuffChangeNotify = _reflection.GeneratedProtocolMessageType('ServerBuffChangeNotify', (_message.Message,), {
  'DESCRIPTOR' : _SERVERBUFFCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.ServerBuffChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:ServerBuffChangeNotify)
  })
_sym_db.RegisterMessage(ServerBuffChangeNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SERVERBUFFCHANGENOTIFY._serialized_start=93
  _SERVERBUFFCHANGENOTIFY._serialized_end=425
  _SERVERBUFFCHANGENOTIFY_SERVERBUFFCHANGETYPE._serialized_start=313
  _SERVERBUFFCHANGENOTIFY_SERVERBUFFCHANGETYPE._serialized_end=425
# @@protoc_insertion_point(module_scope)
