# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/MotionState.proto
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
    'genshin/packet/proto/MotionState.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/MotionState.proto*\xc8\x1b\n\x0bMotionState\x12\x15\n\x11MOTION_STATE_NONE\x10\x00\x12\x16\n\x12MOTION_STATE_RESET\x10\x01\x12\x18\n\x14MOTION_STATE_STANDBY\x10\x02\x12\x1d\n\x19MOTION_STATE_STANDBY_MOVE\x10\x03\x12\x15\n\x11MOTION_STATE_WALK\x10\x04\x12\x14\n\x10MOTION_STATE_RUN\x10\x05\x12\x15\n\x11MOTION_STATE_DASH\x10\x06\x12\x16\n\x12MOTION_STATE_CLIMB\x10\x07\x12\x1b\n\x17MOTION_STATE_CLIMB_JUMP\x10\x08\x12!\n\x1dMOTION_STATE_STANDBY_TO_CLIMB\x10\t\x12\x16\n\x12MOTION_STATE_FIGHT\x10\n\x12\x15\n\x11MOTION_STATE_JUMP\x10\x0b\x12\x15\n\x11MOTION_STATE_DROP\x10\x0c\x12\x14\n\x10MOTION_STATE_FLY\x10\r\x12\x1a\n\x16MOTION_STATE_SWIM_MOVE\x10\x0e\x12\x1a\n\x16MOTION_STATE_SWIM_IDLE\x10\x0f\x12\x1a\n\x16MOTION_STATE_SWIM_DASH\x10\x10\x12\x1a\n\x16MOTION_STATE_SWIM_JUMP\x10\x11\x12\x15\n\x11MOTION_STATE_SLIP\x10\x12\x12\x1c\n\x18MOTION_STATE_GO_UPSTAIRS\x10\x13\x12\x1f\n\x1bMOTION_STATE_FALL_ON_GROUND\x10\x14\x12)\n%MOTION_STATE_JUMP_UP_WALL_FOR_STANDBY\x10\x15\x12\x1e\n\x1aMOTION_STATE_JUMP_OFF_WALL\x10\x16\x12\x1c\n\x18MOTION_STATE_POWERED_FLY\x10\x17\x12\x1c\n\x18MOTION_STATE_LADDER_IDLE\x10\x18\x12\x1c\n\x18MOTION_STATE_LADDER_MOVE\x10\x19\x12\x1c\n\x18MOTION_STATE_LADDER_SLIP\x10\x1a\x12\"\n\x1eMOTION_STATE_STANDBY_TO_LADDER\x10\x1b\x12\"\n\x1eMOTION_STATE_LADDER_TO_STANDBY\x10\x1c\x12\x1f\n\x1bMOTION_STATE_DANGER_STANDBY\x10\x1d\x12$\n MOTION_STATE_DANGER_STANDBY_MOVE\x10\x1e\x12\x1c\n\x18MOTION_STATE_DANGER_WALK\x10\x1f\x12\x1b\n\x17MOTION_STATE_DANGER_RUN\x10 \x12\x1c\n\x18MOTION_STATE_DANGER_DASH\x10!\x12\x1c\n\x18MOTION_STATE_CROUCH_IDLE\x10\"\x12\x1c\n\x18MOTION_STATE_CROUCH_MOVE\x10#\x12\x1c\n\x18MOTION_STATE_CROUCH_ROLL\x10$\x12\x17\n\x13MOTION_STATE_NOTIFY\x10%\x12\x1b\n\x17MOTION_STATE_LAND_SPEED\x10&\x12\x1e\n\x1aMOTION_STATE_MOVE_FAIL_ACK\x10\'\x12\x1a\n\x16MOTION_STATE_WATERFALL\x10(\x12\"\n\x1eMOTION_STATE_DASH_BEFORE_SHAKE\x10)\x12\x19\n\x15MOTION_STATE_SIT_IDLE\x10*\x12\x1e\n\x1aMOTION_STATE_FORCE_SET_POS\x10+\x12!\n\x1dMOTION_STATE_QUEST_FORCE_DRAG\x10,\x12\x1d\n\x19MOTION_STATE_FOLLOW_ROUTE\x10-\x12\x1f\n\x1bMOTION_STATE_SKIFF_BOARDING\x10.\x12\x1d\n\x19MOTION_STATE_SKIFF_NORMAL\x10/\x12\x1b\n\x17MOTION_STATE_SKIFF_DASH\x10\x30\x12#\n\x1fMOTION_STATE_SKIFF_POWERED_DASH\x10\x31\x12 \n\x1cMOTION_STATE_DESTROY_VEHICLE\x10\x32\x12\x19\n\x15MOTION_STATE_FLY_IDLE\x10\x33\x12\x19\n\x15MOTION_STATE_FLY_SLOW\x10\x34\x12\x19\n\x15MOTION_STATE_FLY_FAST\x10\x35\x12\x19\n\x15MOTION_STATE_AIM_MOVE\x10\x36\x12!\n\x1dMOTION_STATE_AIR_COMPENSATION\x10\x37\x12\x1e\n\x1aMOTION_STATE_SORUSH_NORMAL\x10\x38\x12\x1f\n\x1bMOTION_STATE_ROLLER_COASTER\x10\x39\x12\x1a\n\x16MOTION_STATE_DIVE_IDLE\x10:\x12\x1a\n\x16MOTION_STATE_DIVE_MOVE\x10;\x12\x1a\n\x16MOTION_STATE_DIVE_DASH\x10<\x12\x1e\n\x1aMOTION_STATE_DIVE_DOLPHINE\x10=\x12\x16\n\x12MOTION_STATE_DEBUG\x10>\x12\x1e\n\x1aMOTION_STATE_OCEAN_CURRENT\x10?\x12\x1f\n\x1bMOTION_STATE_DIVE_SWIM_MOVE\x10@\x12\x1f\n\x1bMOTION_STATE_DIVE_SWIM_IDLE\x10\x41\x12\x1f\n\x1bMOTION_STATE_DIVE_SWIM_DASH\x10\x42\x12\x1a\n\x16MOTION_STATE_ARC_LIGHT\x10\x43\x12\x1f\n\x1bMOTION_STATE_ARC_LIGHT_SAFE\x10\x44\x12 \n\x1cMOTION_STATE_VEHICLE_STANDBY\x10\x45\x12\x1c\n\x18MOTION_STATE_VEHICLE_RUN\x10\x46\x12\x1d\n\x19MOTION_STATE_VEHICLE_DASH\x10G\x12\x1e\n\x1aMOTION_STATE_VEHICLE_CLIMB\x10H\x12#\n\x1fMOTION_STATE_VEHICLE_CLIMB_JUMP\x10I\x12)\n%MOTION_STATE_VEHICLE_STANDBY_TO_CLIMB\x10J\x12\x1e\n\x1aMOTION_STATE_VEHICLE_FIGHT\x10K\x12\x1d\n\x19MOTION_STATE_VEHICLE_JUMP\x10L\x12\x1d\n\x19MOTION_STATE_VEHICLE_DROP\x10M\x12\x1c\n\x18MOTION_STATE_VEHICLE_FLY\x10N\x12\"\n\x1eMOTION_STATE_VEHICLE_SWIM_MOVE\x10O\x12\"\n\x1eMOTION_STATE_VEHICLE_SWIM_IDLE\x10P\x12\"\n\x1eMOTION_STATE_VEHICLE_SWIM_DASH\x10Q\x12\x1d\n\x19MOTION_STATE_VEHICLE_SLIP\x10R\x12$\n MOTION_STATE_VEHICLE_GO_UPSTAIRS\x10S\x12\'\n#MOTION_STATE_VEHICLE_FALL_ON_GROUND\x10T\x12&\n\"MOTION_STATE_VEHICLE_JUMP_OFF_WALL\x10U\x12$\n MOTION_STATE_VEHICLE_POWERED_FLY\x10V\x12\'\n#MOTION_STATE_VEHICLE_DANGER_STANDBY\x10W\x12#\n\x1fMOTION_STATE_VEHICLE_DANGER_RUN\x10X\x12$\n MOTION_STATE_VEHICLE_DANGER_DASH\x10Y\x12\x1f\n\x1bMOTION_STATE_VEHICLE_NOTIFY\x10Z\x12#\n\x1fMOTION_STATE_VEHICLE_LAND_SPEED\x10[\x12*\n&MOTION_STATE_VEHICLE_DASH_BEFORE_SHAKE\x10\\\x12)\n%MOTION_STATE_VEHICLE_QUEST_FORCE_DRAG\x10]\x12%\n!MOTION_STATE_VEHICLE_FOLLOW_ROUTE\x10^\x12!\n\x1dMOTION_STATE_VEHICLE_FLY_IDLE\x10_\x12!\n\x1dMOTION_STATE_VEHICLE_FLY_SLOW\x10`\x12!\n\x1dMOTION_STATE_VEHICLE_FLY_FAST\x10\x61\x12)\n%MOTION_STATE_VEHICLE_AIR_COMPENSATION\x10\x62\x12\"\n\x1eMOTION_STATE_VEHICLE_ARC_LIGHT\x10\x63\x12\'\n#MOTION_STATE_VEHICLE_ARC_LIGHT_SAFE\x10\x64\x12)\n%MOTION_STATE_VEHICLE_DANGER_SWIM_MOVE\x10\x65\x12)\n%MOTION_STATE_VEHICLE_DANGER_SWIM_IDLE\x10\x66\x12)\n%MOTION_STATE_VEHICLE_DANGER_SWIM_DASH\x10g\x12#\n\x1fMOTION_STATE_FOLLOW_CURVE_ROUTE\x10h\x12+\n\'MOTION_STATE_VEHICLE_FOLLOW_CURVE_ROUTE\x10i\x12!\n\x1dMOTION_STATE_NATSAURUS_NORMAL\x10j\x12#\n\x1fMOTION_STATE_NATSAURUS_ENTERING\x10k\x12\x14\n\x10MOTION_STATE_NUM\x10lB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.MotionState_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_MOTIONSTATE']._serialized_start=43
  _globals['_MOTIONSTATE']._serialized_end=3571
# @@protoc_insertion_point(module_scope)
