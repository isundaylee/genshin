# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EvtCreateGadgetNotify.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'genshin/packet/proto/EvtCreateGadgetNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2
from genshin.packet.proto import AbilityString_pb2 as genshin_dot_packet_dot_proto_dot_AbilityString__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/EvtCreateGadgetNotify.proto\x1a!genshin/packet/proto/Vector.proto\x1a(genshin/packet/proto/AbilityString.proto\x1a&genshin/packet/proto/ForwardType.proto\"\xff\x04\n\x15\x45vtCreateGadgetNotify\x12%\n\x1ctarget_lock_point_index_list\x18\x85\x02 \x03(\r\x12\x19\n\x08init_pos\x18\r \x01(\x0b\x32\x07.Vector\x12\"\n\x11init_euler_angles\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x1e\n\x15target_entity_id_list\x18\xa9\x06 \x03(\r\x12%\n\x0c\x61\x62ility_name\x18\xaa\x03 \x01(\x0b\x32\x0e.AbilityString\x12\x1f\n\x17target_lock_point_index\x18\x08 \x01(\r\x12\"\n\x0c\x66orward_type\x18\x06 \x01(\x0e\x32\x0c.ForwardType\x12\x1f\n\x16is_peer_id_from_player\x18\xfd\x04 \x01(\x08\x12\x16\n\ris_async_load\x18\xe2\x02 \x01(\x08\x12\x1e\n\x16sight_group_with_owner\x18\t \x01(\x08\x12\"\n\x1ais_true_life_time_by_owner\x18\n \x01(\x08\x12\x11\n\tentity_id\x18\x05 \x01(\r\x12\x0f\n\x07room_id\x18\x02 \x01(\r\x12\x15\n\x0cinit_pose_id\x18\xc8\x02 \x01(\r\x12\x1c\n\x14prop_owner_entity_id\x18\x03 \x01(\r\x12\x10\n\x08local_id\x18\x13 \x01(\x05\x12\x18\n\x10target_entity_id\x18\x0c \x01(\r\x12\x11\n\tcamp_type\x18\x07 \x01(\r\x12\x0f\n\x07\x63\x61mp_id\x18\x01 \x01(\r\x12\x14\n\x0bLKHKMKMKMJC\x18\xea\x0e \x01(\r\x12\x17\n\x0fowner_entity_id\x18\x0f \x01(\r\x12\x11\n\tconfig_id\x18\x0e \x01(\r\x12\x0c\n\x04guid\x18\x0b \x01(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EvtCreateGadgetNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_EVTCREATEGADGETNOTIFY']._serialized_start=170
  _globals['_EVTCREATEGADGETNOTIFY']._serialized_end=809
# @@protoc_insertion_point(module_scope)
