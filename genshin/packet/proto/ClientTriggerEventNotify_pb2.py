# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ClientTriggerEventNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EventTriggerType_pb2 as genshin_dot_packet_dot_proto_dot_EventTriggerType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/ClientTriggerEventNotify.proto\x1a+genshin/packet/proto/EventTriggerType.proto\"S\n\x18\x43lientTriggerEventNotify\x12\x10\n\x08\x66orce_id\x18\x03 \x01(\r\x12%\n\nevent_type\x18\x02 \x01(\x0e\x32\x11.EventTriggerTypeB\x16\n\x14org.sorapointa.protob\x06proto3')



_CLIENTTRIGGEREVENTNOTIFY = DESCRIPTOR.message_types_by_name['ClientTriggerEventNotify']
ClientTriggerEventNotify = _reflection.GeneratedProtocolMessageType('ClientTriggerEventNotify', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTRIGGEREVENTNOTIFY,
  '__module__' : 'genshin.packet.proto.ClientTriggerEventNotify_pb2'
  # @@protoc_insertion_point(class_scope:ClientTriggerEventNotify)
  })
_sym_db.RegisterMessage(ClientTriggerEventNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _CLIENTTRIGGEREVENTNOTIFY._serialized_start=100
  _CLIENTTRIGGEREVENTNOTIFY._serialized_end=183
# @@protoc_insertion_point(module_scope)