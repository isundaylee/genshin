# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/AbilityAppliedModifier.proto
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
    'genshin/packet/proto/AbilityAppliedModifier.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AbilityString_pb2 as genshin_dot_packet_dot_proto_dot_AbilityString__pb2
from genshin.packet.proto import AbilityAttachedModifier_pb2 as genshin_dot_packet_dot_proto_dot_AbilityAttachedModifier__pb2
from genshin.packet.proto import ModifierDurability_pb2 as genshin_dot_packet_dot_proto_dot_ModifierDurability__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1genshin/packet/proto/AbilityAppliedModifier.proto\x1a(genshin/packet/proto/AbilityString.proto\x1a\x32genshin/packet/proto/AbilityAttachedModifier.proto\x1a-genshin/packet/proto/ModifierDurability.proto\"\xfe\x03\n\x16\x41\x62ilityAppliedModifier\x12\x19\n\x11modifier_local_id\x18\x01 \x01(\x05\x12 \n\x18parent_ability_entity_id\x18\x02 \x01(\r\x12+\n\x13parent_ability_name\x18\x03 \x01(\x0b\x32\x0e.AbilityString\x12/\n\x17parent_ability_override\x18\x04 \x01(\x0b\x32\x0e.AbilityString\x12\x1c\n\x14instanced_ability_id\x18\x05 \x01(\r\x12\x1d\n\x15instanced_modifier_id\x18\x06 \x01(\r\x12\x16\n\x0e\x65xist_duration\x18\x07 \x01(\x02\x12=\n\x1b\x61ttached_instanced_modifier\x18\x08 \x01(\x0b\x32\x18.AbilityAttachedModifier\x12\x17\n\x0f\x61pply_entity_id\x18\t \x01(\r\x12\"\n\x1ais_attached_parent_ability\x18\n \x01(\x08\x12\x30\n\x13modifier_durability\x18\x0b \x01(\x0b\x32\x13.ModifierDurability\x12\x11\n\tsbuff_uid\x18\x0c \x01(\r\x12\x1e\n\x16is_serverbuff_modifier\x18\r \x01(\x08\x12\x13\n\x0bNCEGKBANOBP\x18\x0e \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.AbilityAppliedModifier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_ABILITYAPPLIEDMODIFIER']._serialized_start=195
  _globals['_ABILITYAPPLIEDMODIFIER']._serialized_end=705
# @@protoc_insertion_point(module_scope)
