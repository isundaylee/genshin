# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AbilityMetaModifierChange.proto
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
    'genshin/packet/proto/AbilityMetaModifierChange.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityString_pb2 as genshin_dot_packet_dot_proto_dot_AbilityString__pb2
from genshin.packet.proto import ModifierProperty_pb2 as genshin_dot_packet_dot_proto_dot_ModifierProperty__pb2
from genshin.packet.proto import AbilityAttachedModifier_pb2 as genshin_dot_packet_dot_proto_dot_AbilityAttachedModifier__pb2
from genshin.packet.proto import ModifierAction_pb2 as genshin_dot_packet_dot_proto_dot_ModifierAction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4genshin/packet/proto/AbilityMetaModifierChange.proto\x1a(genshin/packet/proto/AbilityString.proto\x1a+genshin/packet/proto/ModifierProperty.proto\x1a\x32genshin/packet/proto/AbilityAttachedModifier.proto\x1a)genshin/packet/proto/ModifierAction.proto\"\xc5\x03\n\x19\x41\x62ilityMetaModifierChange\x12\x17\n\x0fserver_buff_uid\x18\x02 \x01(\r\x12/\n\x17parent_ability_override\x18\x03 \x01(\x0b\x32\x0e.AbilityString\x12%\n\nproperties\x18\x04 \x03(\x0b\x32\x11.ModifierProperty\x12\x17\n\x0f\x61pply_entity_id\x18\x05 \x01(\r\x12=\n\x1b\x61ttached_instanced_modifier\x18\x06 \x01(\x0b\x32\x18.AbilityAttachedModifier\x12+\n\x13parent_ability_name\x18\x07 \x01(\x0b\x32\x0e.AbilityString\x12\x19\n\x11modifier_local_id\x18\x08 \x01(\x05\x12\"\n\x1ais_attached_parent_ability\x18\n \x01(\x08\x12\x13\n\x0b\x45\x46ONMKFIJNA\x18\x0b \x01(\x08\x12\x13\n\x0bMAPJDCOAIMG\x18\x0c \x01(\x08\x12\x13\n\x0bKKAAMMJBABH\x18\r \x01(\x02\x12\x13\n\x0bKKFHAIPCCFA\x18\x0e \x01(\x04\x12\x1f\n\x06\x61\x63tion\x18\x0f \x01(\x0e\x32\x0f.ModifierActionB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AbilityMetaModifierChange_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ABILITYMETAMODIFIERCHANGE']._serialized_start=239
  _globals['_ABILITYMETAMODIFIERCHANGE']._serialized_end=692
# @@protoc_insertion_point(module_scope)
