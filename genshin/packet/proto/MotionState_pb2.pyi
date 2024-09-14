from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MotionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTION_STATE_NONE: _ClassVar[MotionState]
    MOTION_STATE_RESET: _ClassVar[MotionState]
    MOTION_STATE_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_STANDBY_MOVE: _ClassVar[MotionState]
    MOTION_STATE_WALK: _ClassVar[MotionState]
    MOTION_STATE_RUN: _ClassVar[MotionState]
    MOTION_STATE_DASH: _ClassVar[MotionState]
    MOTION_STATE_CLIMB: _ClassVar[MotionState]
    MOTION_STATE_CLIMB_JUMP: _ClassVar[MotionState]
    MOTION_STATE_STANDBY_TO_CLIMB: _ClassVar[MotionState]
    MOTION_STATE_FIGHT: _ClassVar[MotionState]
    MOTION_STATE_JUMP: _ClassVar[MotionState]
    MOTION_STATE_DROP: _ClassVar[MotionState]
    MOTION_STATE_FLY: _ClassVar[MotionState]
    MOTION_STATE_SWIM_MOVE: _ClassVar[MotionState]
    MOTION_STATE_SWIM_IDLE: _ClassVar[MotionState]
    MOTION_STATE_SWIM_DASH: _ClassVar[MotionState]
    MOTION_STATE_SWIM_JUMP: _ClassVar[MotionState]
    MOTION_STATE_SLIP: _ClassVar[MotionState]
    MOTION_STATE_GO_UPSTAIRS: _ClassVar[MotionState]
    MOTION_STATE_FALL_ON_GROUND: _ClassVar[MotionState]
    MOTION_STATE_JUMP_UP_WALL_FOR_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_JUMP_OFF_WALL: _ClassVar[MotionState]
    MOTION_STATE_POWERED_FLY: _ClassVar[MotionState]
    MOTION_STATE_LADDER_IDLE: _ClassVar[MotionState]
    MOTION_STATE_LADDER_MOVE: _ClassVar[MotionState]
    MOTION_STATE_LADDER_SLIP: _ClassVar[MotionState]
    MOTION_STATE_STANDBY_TO_LADDER: _ClassVar[MotionState]
    MOTION_STATE_LADDER_TO_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_DANGER_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_DANGER_STANDBY_MOVE: _ClassVar[MotionState]
    MOTION_STATE_DANGER_WALK: _ClassVar[MotionState]
    MOTION_STATE_DANGER_RUN: _ClassVar[MotionState]
    MOTION_STATE_DANGER_DASH: _ClassVar[MotionState]
    MOTION_STATE_CROUCH_IDLE: _ClassVar[MotionState]
    MOTION_STATE_CROUCH_MOVE: _ClassVar[MotionState]
    MOTION_STATE_CROUCH_ROLL: _ClassVar[MotionState]
    MOTION_STATE_NOTIFY: _ClassVar[MotionState]
    MOTION_STATE_LAND_SPEED: _ClassVar[MotionState]
    MOTION_STATE_MOVE_FAIL_ACK: _ClassVar[MotionState]
    MOTION_STATE_WATERFALL: _ClassVar[MotionState]
    MOTION_STATE_DASH_BEFORE_SHAKE: _ClassVar[MotionState]
    MOTION_STATE_SIT_IDLE: _ClassVar[MotionState]
    MOTION_STATE_FORCE_SET_POS: _ClassVar[MotionState]
    MOTION_STATE_QUEST_FORCE_DRAG: _ClassVar[MotionState]
    MOTION_STATE_FOLLOW_ROUTE: _ClassVar[MotionState]
    MOTION_STATE_SKIFF_BOARDING: _ClassVar[MotionState]
    MOTION_STATE_SKIFF_NORMAL: _ClassVar[MotionState]
    MOTION_STATE_SKIFF_DASH: _ClassVar[MotionState]
    MOTION_STATE_SKIFF_POWERED_DASH: _ClassVar[MotionState]
    MOTION_STATE_DESTROY_VEHICLE: _ClassVar[MotionState]
    MOTION_STATE_FLY_IDLE: _ClassVar[MotionState]
    MOTION_STATE_FLY_SLOW: _ClassVar[MotionState]
    MOTION_STATE_FLY_FAST: _ClassVar[MotionState]
    MOTION_STATE_AIM_MOVE: _ClassVar[MotionState]
    MOTION_STATE_AIR_COMPENSATION: _ClassVar[MotionState]
    MOTION_STATE_SORUSH_NORMAL: _ClassVar[MotionState]
    MOTION_STATE_ROLLER_COASTER: _ClassVar[MotionState]
    MOTION_STATE_DIVE_IDLE: _ClassVar[MotionState]
    MOTION_STATE_DIVE_MOVE: _ClassVar[MotionState]
    MOTION_STATE_DIVE_DASH: _ClassVar[MotionState]
    MOTION_STATE_DIVE_DOLPHINE: _ClassVar[MotionState]
    MOTION_STATE_DEBUG: _ClassVar[MotionState]
    MOTION_STATE_OCEAN_CURRENT: _ClassVar[MotionState]
    MOTION_STATE_DIVE_SWIM_MOVE: _ClassVar[MotionState]
    MOTION_STATE_DIVE_SWIM_IDLE: _ClassVar[MotionState]
    MOTION_STATE_DIVE_SWIM_DASH: _ClassVar[MotionState]
    MOTION_STATE_ARC_LIGHT: _ClassVar[MotionState]
    MOTION_STATE_ARC_LIGHT_SAFE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_RUN: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DASH: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_CLIMB: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_CLIMB_JUMP: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_STANDBY_TO_CLIMB: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FIGHT: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_JUMP: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DROP: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FLY: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_SWIM_MOVE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_SWIM_IDLE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_SWIM_DASH: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_SLIP: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_GO_UPSTAIRS: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FALL_ON_GROUND: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_JUMP_OFF_WALL: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_POWERED_FLY: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_STANDBY: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_RUN: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_DASH: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_NOTIFY: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_LAND_SPEED: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DASH_BEFORE_SHAKE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_QUEST_FORCE_DRAG: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FOLLOW_ROUTE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FLY_IDLE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FLY_SLOW: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FLY_FAST: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_AIR_COMPENSATION: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_ARC_LIGHT: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_ARC_LIGHT_SAFE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_SWIM_MOVE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_SWIM_IDLE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_DANGER_SWIM_DASH: _ClassVar[MotionState]
    MOTION_STATE_FOLLOW_CURVE_ROUTE: _ClassVar[MotionState]
    MOTION_STATE_VEHICLE_FOLLOW_CURVE_ROUTE: _ClassVar[MotionState]
    MOTION_STATE_NATSAURUS_NORMAL: _ClassVar[MotionState]
    MOTION_STATE_NATSAURUS_ENTERING: _ClassVar[MotionState]
    MOTION_STATE_NUM: _ClassVar[MotionState]
MOTION_STATE_NONE: MotionState
MOTION_STATE_RESET: MotionState
MOTION_STATE_STANDBY: MotionState
MOTION_STATE_STANDBY_MOVE: MotionState
MOTION_STATE_WALK: MotionState
MOTION_STATE_RUN: MotionState
MOTION_STATE_DASH: MotionState
MOTION_STATE_CLIMB: MotionState
MOTION_STATE_CLIMB_JUMP: MotionState
MOTION_STATE_STANDBY_TO_CLIMB: MotionState
MOTION_STATE_FIGHT: MotionState
MOTION_STATE_JUMP: MotionState
MOTION_STATE_DROP: MotionState
MOTION_STATE_FLY: MotionState
MOTION_STATE_SWIM_MOVE: MotionState
MOTION_STATE_SWIM_IDLE: MotionState
MOTION_STATE_SWIM_DASH: MotionState
MOTION_STATE_SWIM_JUMP: MotionState
MOTION_STATE_SLIP: MotionState
MOTION_STATE_GO_UPSTAIRS: MotionState
MOTION_STATE_FALL_ON_GROUND: MotionState
MOTION_STATE_JUMP_UP_WALL_FOR_STANDBY: MotionState
MOTION_STATE_JUMP_OFF_WALL: MotionState
MOTION_STATE_POWERED_FLY: MotionState
MOTION_STATE_LADDER_IDLE: MotionState
MOTION_STATE_LADDER_MOVE: MotionState
MOTION_STATE_LADDER_SLIP: MotionState
MOTION_STATE_STANDBY_TO_LADDER: MotionState
MOTION_STATE_LADDER_TO_STANDBY: MotionState
MOTION_STATE_DANGER_STANDBY: MotionState
MOTION_STATE_DANGER_STANDBY_MOVE: MotionState
MOTION_STATE_DANGER_WALK: MotionState
MOTION_STATE_DANGER_RUN: MotionState
MOTION_STATE_DANGER_DASH: MotionState
MOTION_STATE_CROUCH_IDLE: MotionState
MOTION_STATE_CROUCH_MOVE: MotionState
MOTION_STATE_CROUCH_ROLL: MotionState
MOTION_STATE_NOTIFY: MotionState
MOTION_STATE_LAND_SPEED: MotionState
MOTION_STATE_MOVE_FAIL_ACK: MotionState
MOTION_STATE_WATERFALL: MotionState
MOTION_STATE_DASH_BEFORE_SHAKE: MotionState
MOTION_STATE_SIT_IDLE: MotionState
MOTION_STATE_FORCE_SET_POS: MotionState
MOTION_STATE_QUEST_FORCE_DRAG: MotionState
MOTION_STATE_FOLLOW_ROUTE: MotionState
MOTION_STATE_SKIFF_BOARDING: MotionState
MOTION_STATE_SKIFF_NORMAL: MotionState
MOTION_STATE_SKIFF_DASH: MotionState
MOTION_STATE_SKIFF_POWERED_DASH: MotionState
MOTION_STATE_DESTROY_VEHICLE: MotionState
MOTION_STATE_FLY_IDLE: MotionState
MOTION_STATE_FLY_SLOW: MotionState
MOTION_STATE_FLY_FAST: MotionState
MOTION_STATE_AIM_MOVE: MotionState
MOTION_STATE_AIR_COMPENSATION: MotionState
MOTION_STATE_SORUSH_NORMAL: MotionState
MOTION_STATE_ROLLER_COASTER: MotionState
MOTION_STATE_DIVE_IDLE: MotionState
MOTION_STATE_DIVE_MOVE: MotionState
MOTION_STATE_DIVE_DASH: MotionState
MOTION_STATE_DIVE_DOLPHINE: MotionState
MOTION_STATE_DEBUG: MotionState
MOTION_STATE_OCEAN_CURRENT: MotionState
MOTION_STATE_DIVE_SWIM_MOVE: MotionState
MOTION_STATE_DIVE_SWIM_IDLE: MotionState
MOTION_STATE_DIVE_SWIM_DASH: MotionState
MOTION_STATE_ARC_LIGHT: MotionState
MOTION_STATE_ARC_LIGHT_SAFE: MotionState
MOTION_STATE_VEHICLE_STANDBY: MotionState
MOTION_STATE_VEHICLE_RUN: MotionState
MOTION_STATE_VEHICLE_DASH: MotionState
MOTION_STATE_VEHICLE_CLIMB: MotionState
MOTION_STATE_VEHICLE_CLIMB_JUMP: MotionState
MOTION_STATE_VEHICLE_STANDBY_TO_CLIMB: MotionState
MOTION_STATE_VEHICLE_FIGHT: MotionState
MOTION_STATE_VEHICLE_JUMP: MotionState
MOTION_STATE_VEHICLE_DROP: MotionState
MOTION_STATE_VEHICLE_FLY: MotionState
MOTION_STATE_VEHICLE_SWIM_MOVE: MotionState
MOTION_STATE_VEHICLE_SWIM_IDLE: MotionState
MOTION_STATE_VEHICLE_SWIM_DASH: MotionState
MOTION_STATE_VEHICLE_SLIP: MotionState
MOTION_STATE_VEHICLE_GO_UPSTAIRS: MotionState
MOTION_STATE_VEHICLE_FALL_ON_GROUND: MotionState
MOTION_STATE_VEHICLE_JUMP_OFF_WALL: MotionState
MOTION_STATE_VEHICLE_POWERED_FLY: MotionState
MOTION_STATE_VEHICLE_DANGER_STANDBY: MotionState
MOTION_STATE_VEHICLE_DANGER_RUN: MotionState
MOTION_STATE_VEHICLE_DANGER_DASH: MotionState
MOTION_STATE_VEHICLE_NOTIFY: MotionState
MOTION_STATE_VEHICLE_LAND_SPEED: MotionState
MOTION_STATE_VEHICLE_DASH_BEFORE_SHAKE: MotionState
MOTION_STATE_VEHICLE_QUEST_FORCE_DRAG: MotionState
MOTION_STATE_VEHICLE_FOLLOW_ROUTE: MotionState
MOTION_STATE_VEHICLE_FLY_IDLE: MotionState
MOTION_STATE_VEHICLE_FLY_SLOW: MotionState
MOTION_STATE_VEHICLE_FLY_FAST: MotionState
MOTION_STATE_VEHICLE_AIR_COMPENSATION: MotionState
MOTION_STATE_VEHICLE_ARC_LIGHT: MotionState
MOTION_STATE_VEHICLE_ARC_LIGHT_SAFE: MotionState
MOTION_STATE_VEHICLE_DANGER_SWIM_MOVE: MotionState
MOTION_STATE_VEHICLE_DANGER_SWIM_IDLE: MotionState
MOTION_STATE_VEHICLE_DANGER_SWIM_DASH: MotionState
MOTION_STATE_FOLLOW_CURVE_ROUTE: MotionState
MOTION_STATE_VEHICLE_FOLLOW_CURVE_ROUTE: MotionState
MOTION_STATE_NATSAURUS_NORMAL: MotionState
MOTION_STATE_NATSAURUS_ENTERING: MotionState
MOTION_STATE_NUM: MotionState