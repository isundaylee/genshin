# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtSetAttackTargetNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import EvtSetAttackTargetInfo_pb2 as genshin_dot_packet_dot_proto_dot_EvtSetAttackTargetInfo__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/EvtSetAttackTargetNotify.proto\x1a\x31genshin/packet/proto/EvtSetAttackTargetInfo.proto\x1a&genshin/packet/proto/ForwardType.proto\"{\n\x18\x45vtSetAttackTargetNotify\x12\"\n\x0c\x66orward_type\x18\x01 \x01(\x0e\x32\x0c.ForwardType\x12;\n\x1a\x65vt_set_attack_target_info\x18\x0b \x01(\x0b\x32\x17.EvtSetAttackTargetInfoB\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTSETATTACKTARGETNOTIFY = DESCRIPTOR.message_types_by_name['EvtSetAttackTargetNotify']
EvtSetAttackTargetNotify = _reflection.GeneratedProtocolMessageType('EvtSetAttackTargetNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTSETATTACKTARGETNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtSetAttackTargetNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtSetAttackTargetNotify)
  })
_sym_db.RegisterMessage(EvtSetAttackTargetNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTSETATTACKTARGETNOTIFY._serialized_start=146
  _EVTSETATTACKTARGETNOTIFY._serialized_end=269
# @@protoc_insertion_point(module_scope)
