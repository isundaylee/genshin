# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EvtBulletHitNotify.proto
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
    'genshin/packet/proto/EvtBulletHitNotify.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HitColliderType_pb2 as genshin_dot_packet_dot_proto_dot_HitColliderType__pb2
from genshin.packet.proto import ForwardType_pb2 as genshin_dot_packet_dot_proto_dot_ForwardType__pb2
from genshin.packet.proto import Vector_pb2 as genshin_dot_packet_dot_proto_dot_Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/EvtBulletHitNotify.proto\x1a*genshin/packet/proto/HitColliderType.proto\x1a&genshin/packet/proto/ForwardType.proto\x1a!genshin/packet/proto/Vector.proto\"\x98\x02\n\x12\x45vtBulletHitNotify\x12\x18\n\x10single_bullet_id\x18\x04 \x01(\r\x12\x14\n\x0c\x66orward_peer\x18\x05 \x01(\r\x12\x15\n\rhit_box_index\x18\x07 \x01(\x05\x12+\n\x11hit_collider_type\x18\t \x01(\x0e\x32\x10.HitColliderType\x12\x11\n\tentity_id\x18\n \x01(\r\x12\"\n\x0c\x66orward_type\x18\x0b \x01(\x0e\x32\x0c.ForwardType\x12\x1a\n\thit_point\x18\r \x01(\x0b\x32\x07.Vector\x12\x15\n\rhit_entity_id\x18\x0e \x01(\r\x12$\n\x13hit_pointhit_normal\x18\x0f \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EvtBulletHitNotify_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_EVTBULLETHITNOTIFY']._serialized_start=169
  _globals['_EVTBULLETHITNOTIFY']._serialized_end=449
# @@protoc_insertion_point(module_scope)
