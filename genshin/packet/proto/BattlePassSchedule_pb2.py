# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/BattlePassSchedule.proto
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
    'genshin/packet/proto/BattlePassSchedule.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BattlePassCycle_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassCycle__pb2
from genshin.packet.proto import BattlePassRewardPlanOption_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassRewardPlanOption__pb2
from genshin.packet.proto import BattlePassProduct_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassProduct__pb2
from genshin.packet.proto import BattlePassRewardTag_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassRewardTag__pb2
from genshin.packet.proto import BattlePassUnlockStatus_pb2 as genshin_dot_packet_dot_proto_dot_BattlePassUnlockStatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-genshin/packet/proto/BattlePassSchedule.proto\x1a*genshin/packet/proto/BattlePassCycle.proto\x1a\x35genshin/packet/proto/BattlePassRewardPlanOption.proto\x1a,genshin/packet/proto/BattlePassProduct.proto\x1a.genshin/packet/proto/BattlePassRewardTag.proto\x1a\x31genshin/packet/proto/BattlePassUnlockStatus.proto\"\xde\x03\n\x12\x42\x61ttlePassSchedule\x12#\n\tcur_cycle\x18\x01 \x01(\x0b\x32\x10.BattlePassCycle\x12<\n\x17reward_plan_option_list\x18\x02 \x03(\x0b\x32\x1b.BattlePassRewardPlanOption\x12(\n\x0cproduct_info\x18\x03 \x01(\x0b\x32\x12.BattlePassProduct\x12\x13\n\x0bLOPPMEONNEG\x18\x04 \x01(\x08\x12/\n\x11reward_taken_list\x18\x05 \x03(\x0b\x32\x14.BattlePassRewardTag\x12\x18\n\x10\x63ur_cycle_points\x18\x06 \x01(\r\x12\x12\n\nbegin_time\x18\x07 \x01(\r\x12\"\n\x1ais_extra_paid_reward_taken\x18\x08 \x01(\x08\x12\x10\n\x08\x65nd_time\x18\t \x01(\r\x12\r\n\x05point\x18\n \x01(\r\x12\x1b\n\x13paid_platform_flags\x18\x0b \x01(\r\x12\x13\n\x0bschedule_id\x18\x0c \x01(\r\x12\x11\n\tis_viewed\x18\r \x01(\x08\x12.\n\runlock_status\x18\x0e \x01(\x0e\x32\x17.BattlePassUnlockStatus\x12\r\n\x05level\x18\x0f \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.BattlePassSchedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BATTLEPASSSCHEDULE']._serialized_start=294
  _globals['_BATTLEPASSSCHEDULE']._serialized_end=772
# @@protoc_insertion_point(module_scope)
