# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtEntityRenderersChangedNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EntityRendererChangedInfo_pb2 as genshin_dot_packet_dot_proto_dot_EntityRendererChangedInfo__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:genshin/packet/proto/EvtEntityRenderersChangedNotify.proto\x1a\x34genshin/packet/proto/EntityRendererChangedInfo.proto\x1a&genshin/packet/proto/ForwardType.proto\"\xac\x01\n\x1f\x45vtEntityRenderersChangedNotify\x12\"\n\x0c\x66orward_type\x18\x08 \x01(\x0e\x32\x0c.ForwardType\x12\x11\n\tentity_id\x18\x0f \x01(\r\x12\x17\n\x0fis_server_cache\x18\x03 \x01(\x08\x12\x39\n\x15renderer_changed_info\x18\x05 \x01(\x0b\x32\x1a.EntityRendererChangedInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_EVTENTITYRENDERERSCHANGEDNOTIFY = DESCRIPTOR.message_types_by_name['EvtEntityRenderersChangedNotify']
EvtEntityRenderersChangedNotify = _reflection.GeneratedProtocolMessageType('EvtEntityRenderersChangedNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTENTITYRENDERERSCHANGEDNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtEntityRenderersChangedNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtEntityRenderersChangedNotify)
  })
_sym_db.RegisterMessage(EvtEntityRenderersChangedNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _EVTENTITYRENDERERSCHANGEDNOTIFY._serialized_start=157
  _EVTENTITYRENDERERSCHANGEDNOTIFY._serialized_end=329
# @@protoc_insertion_point(module_scope)
