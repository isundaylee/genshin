# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/EvtAvatarEnterFocusNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/EvtAvatarEnterFocusNotify.proto\x1a&genshin/packet/proto/ForwardType.proto\x1a!genshin/packet/proto/Vector.proto\"\xed\x02\n\x19\x45vtAvatarEnterFocusNotify\x12\x11\n\tentity_id\x18\x01 \x01(\r\x12\x10\n\x08\x63\x61n_move\x18\n \x01(\x08\x12!\n\x19\x65nter_holding_focus_shoot\x18\r \x01(\x08\x12\x1b\n\x13Unk2700_GACKGHEHEIK\x18\x06 \x01(\x08\x12\x16\n\x0euse_auto_focus\x18\x05 \x01(\x08\x12\x12\n\nfast_focus\x18\x03 \x01(\x08\x12\x17\n\x0fshow_cross_hair\x18\x0c \x01(\x08\x12 \n\x18\x65nter_normal_focus_shoot\x18\x0e \x01(\x08\x12\"\n\x0c\x66orward_type\x18\x08 \x01(\x0e\x32\x0c.ForwardType\x12\x1e\n\rfocus_forward\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x14\n\x0c\x64isable_anim\x18\t \x01(\x08\x12\x18\n\x10use_focus_sticky\x18\x0f \x01(\x08\x12\x10\n\x08use_gyro\x18\x0b \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_EVTAVATARENTERFOCUSNOTIFY = DESCRIPTOR.message_types_by_name['EvtAvatarEnterFocusNotify']
EvtAvatarEnterFocusNotify = _reflection.GeneratedProtocolMessageType('EvtAvatarEnterFocusNotify', (_message.Message,), {
  'DESCRIPTOR' : _EVTAVATARENTERFOCUSNOTIFY,
  '__module__' : 'genshin.packet.proto.EvtAvatarEnterFocusNotify_pb2'
  # @@protoc_insertion_point(class_scope:EvtAvatarEnterFocusNotify)
  })
_sym_db.RegisterMessage(EvtAvatarEnterFocusNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _EVTAVATARENTERFOCUSNOTIFY._serialized_start=132
  _EVTAVATARENTERFOCUSNOTIFY._serialized_end=497
# @@protoc_insertion_point(module_scope)