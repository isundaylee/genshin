# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ForgeDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ForgeQueueData_pb2 as genshin_dot_packet_dot_proto_dot_ForgeQueueData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*genshin/packet/proto/ForgeDataNotify.proto\x1a)genshin/packet/proto/ForgeQueueData.proto\"\xc4\x01\n\x0f\x46orgeDataNotify\x12\x15\n\rforge_id_list\x18\x05 \x03(\r\x12<\n\x0f\x66orge_queue_map\x18\x08 \x03(\x0b\x32#.ForgeDataNotify.ForgeQueueMapEntry\x12\x15\n\rmax_queue_num\x18\x0e \x01(\r\x1a\x45\n\x12\x46orgeQueueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.ForgeQueueData:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_FORGEDATANOTIFY = DESCRIPTOR.message_types_by_name['ForgeDataNotify']
_FORGEDATANOTIFY_FORGEQUEUEMAPENTRY = _FORGEDATANOTIFY.nested_types_by_name['ForgeQueueMapEntry']
ForgeDataNotify = _reflection.GeneratedProtocolMessageType('ForgeDataNotify', (_message.Message,), {

  'ForgeQueueMapEntry' : _reflection.GeneratedProtocolMessageType('ForgeQueueMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _FORGEDATANOTIFY_FORGEQUEUEMAPENTRY,
    '__module__' : 'genshin.packet.proto.ForgeDataNotify_pb2'
    # @@protoc_insertion_point(class_scope:ForgeDataNotify.ForgeQueueMapEntry)
    })
  ,
  'DESCRIPTOR' : _FORGEDATANOTIFY,
  '__module__' : 'genshin.packet.proto.ForgeDataNotify_pb2'
  # @@protoc_insertion_point(class_scope:ForgeDataNotify)
  })
_sym_db.RegisterMessage(ForgeDataNotify)
_sym_db.RegisterMessage(ForgeDataNotify.ForgeQueueMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _FORGEDATANOTIFY_FORGEQUEUEMAPENTRY._options = None
  _FORGEDATANOTIFY_FORGEQUEUEMAPENTRY._serialized_options = b'8\001'
  _FORGEDATANOTIFY._serialized_start=90
  _FORGEDATANOTIFY._serialized_end=286
  _FORGEDATANOTIFY_FORGEQUEUEMAPENTRY._serialized_start=217
  _FORGEDATANOTIFY_FORGEQUEUEMAPENTRY._serialized_end=286
# @@protoc_insertion_point(module_scope)
